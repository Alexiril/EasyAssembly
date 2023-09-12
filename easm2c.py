from os import mkdir
from os.path import isdir, join
from struct import pack, unpack

from antlr4.Parser import ParserRuleContext  # type: ignore

from easmLexer import easmLexer
from easmParser import ErrorNode, TerminalNode, easmParser
from shared import (SharedBuilder, SharedException,
                    SharedExceptionLevel, SharedId,
                    SharedRules, SharedHandler, SharedRunner,
                    SharedTranslator)

easm2cVersion: tuple[int, int, int] = (0, 2, 0)

easm2cRuntime = """
#ifndef __EASM_RUNTIME
#define __EASM_RUNTIME
#include <stdint.h>
#include <malloc.h>
typedef struct stackNode { int64_t data; struct stackNode* next; } stackNode;
stackNode* stackTop = NULL;
int64_t __easm_ssize = 0;
uint64_t easm_ssize() {
    return __easm_ssize;
}
int64_t easm_spull() {
    if (stackTop == NULL)
        return 0;
    stackNode* temp = stackTop;
    int64_t data = temp->data;
    stackTop = stackTop->next;
    free(temp);
    __easm_ssize--;
    return data;
}
void easm_spush(int64_t num) {
    stackNode* nptr = (stackNode*)malloc(sizeof(stackNode));
    if (nptr == NULL)
        return;
    nptr->data = num;
    nptr->next = stackTop;
    __easm_ssize++;
    stackTop = nptr;
}
#endif

"""

"""
    Exceptions:
    VEN0 - Visit error node exception
    FSN0 - Functions cannot have the same name
    SSN0 - Structures cannot have the same name
    LSN0 - Labels inside one function cannot have the same name
    LFN0 - Label was not found in the function
    RFV0 - Reminder of two non-integral
    SFV0 - Right shift with two non-integral
    SFV1 - Left shift with two non-integral
    PGE0 - CMake errors while generating solution / project
    NCC0 - CMake is not installed (or not installed properly)
    LCV0 - Local call cannot return a value
"""


class easm2cTranslator(SharedTranslator):

    def __init__(self, ids: SharedId, rules: SharedRules, filecode: str, filename: str) -> None:
        super().__init__(ids, rules, filecode, filename)
        self.terminals: list[TerminalNode | str] = list()
        self.expressions: list[str] = []
        self.newLocalObjects: list[str] = list()
        self.initializedLocals: set[str] = set()
        self.doubleResult: bool = False
        self.neededStructures: set[str] = set()
        self.labels: dict[str, set[str]] = dict()
        self.labelsInFunction: set[str] = set()
        self.neededLabels: set[str] = set()
        
        
    def handleException(self, code: str, level: SharedExceptionLevel, ctx: TerminalNode | ParserRuleContext, msg: str) -> None:
        line: int = 0
        column: int = 0

        if type(ctx) == TerminalNode:
            line = ctx.getSymbol().line  # type: ignore
            column = ctx.getSymbol().column  # type: ignore
        elif ParserRuleContext in type(ctx).__bases__:
            line = ctx.start.line  # type: ignore
            column = ctx.start.column  # type: ignore

        self.exceptions.append(
            SharedException(
                code,
                level,
                line,  # type: ignore
                column,  # type: ignore
                self.filename,
                msg
            )
        )

    def visitErrorNode(self, node: ErrorNode) -> None:
        self.handleException(
            "VEN0",
            SharedExceptionLevel.Error,
            node,
            f"Unexpected expression: \"{node}\""
        )

    def visitTerminal(self, node: TerminalNode | str) -> None:
        if node.getSymbol().type == easmLexer.FConst:  # type: ignore
            packed: bytes = pack('d', float(node.getText()))  # type: ignore
            node = hex(unpack('Q', packed)[0]) # type: ignore
        elif node.getSymbol().type == easmLexer.Id:  # type: ignore
            node.getSymbol().text = self.ids.decoupleId(node.getText())  # type: ignore
            if not self.rules.decoupleIDs:
                node.getSymbol().text = self.ids.getId(node.getText())  # type: ignore
        self.terminals.append(node)

    def enterProgram(self, ctx: easmParser.ProgramContext) -> None:
        self.result.append(f"// File: '{self.filename}'")
        self.result.append("// < Auto generated using EASM2C >")
        self.result.append(f"#ifndef {self.filecode}_H")
        self.result.append(f"#define {self.filecode}_H\n")
        
        for _ in range(5):
            self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitProgram(self, ctx: easmParser.ProgramContext) -> None:
        self.result.append("#endif")
        self.result.append("// < Auto generated using EASM2C >\n")
        
        for _ in range(3):
            self.expressionConnection.append(ctx.stop.line) # type: ignore

    def exitFunction(self, ctx: easmParser.FunctionContext) -> None:
        functionName: str = str(self.terminals.pop())
        self.terminals.pop()  # 'func' word

        if functionName in self.functions:
            self.handleException("FSN0", SharedExceptionLevel.Error, ctx,
                                 f"Functions cannot have the same name: {self.ids.getId(functionName)}")

        self.functions.add(functionName)

        for initLocal in self.initializedLocals:
            self.expressions.insert(
                0, f"int64_t {initLocal} = 0; // {self.ids.getId(initLocal)}")
        
        for _ in range(len(self.initializedLocals)):
            self.expressionConnection.append(ctx.start.line) # type: ignore

        if self.doubleResult:
            self.expressions.insert(0, "double dbres = 0;")
            self.expressionConnection.append(ctx.start.line) # type: ignore
        self.doubleResult = False

        for localObject in self.newLocalObjects:
            self.expressions.append(f"if ((void *){localObject} != NULL)")
            self.expressions.append(f"    free((void *){localObject});")
        for _ in range(len(self.newLocalObjects) * 2):
            self.expressionConnection.append(ctx.start.line) # type: ignore
        self.newLocalObjects.clear()

        self.expressions.append("return;")
        self.expressionConnection.append(ctx.start.line) # type: ignore
        expressions: str = '\n    '.join(self.expressions)

        funcInC: str = f"void {functionName} () {{\n    {expressions}  \n}}\n"

        self.expressions.clear()

        self.labels[functionName] = self.labelsInFunction

        for label in self.neededLabels:
            if not label in self.labelsInFunction:
                self.handleException("LFN0", SharedExceptionLevel.Error, ctx,
                                     f"Label is not found in the function: {self.ids.getId(label)}")

        self.labelsInFunction.clear()
        self.neededLabels.clear()
        self.initializedLocals.clear()

        self.result.append(
            f"// {self.ids.getId(functionName)}")

        self.result.append(funcInC)

        for _ in range(5):
            self.expressionConnection.append(ctx.start.line) # type: ignore

        if self.ids.getId(functionName) == "main":
            self.result.append("int main() {")
            self.result.append(f"    {functionName}();")
            self.result.append("    return 0;")
            self.result.append("}")
            for _ in range(4):
                self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitImportStat(self, ctx: easmParser.ImportStatContext) -> None:
        value = str(self.terminals.pop())
        self.terminals.pop()  # 'native' or 'import' word (depends on context)

        if ctx.getChildCount() == 3:
            self.terminals.pop()  # 'import' word
            self.result.append(f"#include {value}")
            self.expressionConnection.append(ctx.start.line) # type: ignore
        else:
            self.imports.add(value.replace('"', ''))

    def exitStructure(self, ctx: easmParser.StructureContext) -> None:
        elements: list[str] = [str(self.terminals.pop())
                               for _ in range(ctx.getChildCount() - 2)]
        structureName = str(self.terminals.pop())
        self.terminals.pop()  # 'struct' word

        if structureName in self.structures:
            self.handleException("SSN0", SharedExceptionLevel.Error, ctx,
                                 f"Structures cannot have the same name: {structureName}")

        self.structures.add(structureName)
        for index in range(len(elements)):
            elements[index] = f"{elements[index]}; // {self.ids.getId(elements[index].split()[1])}\n"
        stringInside: str = "    ".join(elements[::-1])
        for _ in range(len(elements)):
            self.expressionConnection.append(ctx.start.line) # type: ignore

        self.result.append(
            f"// {self.ids.getId(structureName)}")
        self.result.append(f"typedef struct {structureName} {{")
        self.result.append(f"    {stringInside}")
        self.result.append(f"}} {structureName};\n")
        for index in range(4):
            self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitDataTypeDeclaration(self, ctx: easmParser.DataTypeDeclarationContext) -> None:
        value = str(self.terminals.pop())
        kind = str(self.terminals.pop())
        self.terminals.append(f"{kind} {value}")

    def exitLabel(self, ctx: easmParser.LabelContext) -> None:
        self.terminals.pop()  # ':' symbol
        label = str(self.terminals.pop())

        if label in self.labelsInFunction:
            self.handleException("LSN0", SharedExceptionLevel.Error, ctx,
                                 f"Labels inside one function cannot have the same name: {self.ids.getId(label)}")
        self.labelsInFunction.add(label)

        self.expressions.append(f"{label}: // {self.ids.getId(label)}")
        self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitCall(self, ctx: easmParser.CallContext) -> None:
        cstring = ""
        lastTerminal = str(self.terminals.pop())
        invoke = False
        if lastTerminal == ")":
            invoke = True
            params_count = ctx.getChildCount() - 4
            params: list[str] = list()
            for i in range(params_count):
                value = str(self.terminals.pop())
                if i % 2 == 0:
                    params.append(value)
            self.terminals.pop()  # '(' symbol
            funcToInvoke = str(self.terminals.pop())
            cstring = f"{self.ids.getId(funcToInvoke)}({','.join(params[::-1])})"
        else:
            cstring = f"{lastTerminal} ()"
        
        self.terminals.pop()  # 'call' word    
        
        if type(ctx.parentCtx) == easmParser.RvalueContext:  # type: ignore
                if not invoke:
                    self.handleException("LCV0", SharedExceptionLevel.Error, ctx,
                                 f"Local call cannot return a value: call {self.ids.getId(lastTerminal)}")
                self.terminals.append(cstring)
        else:
            self.expressions.append(cstring + ";")
            self.expressionConnection.append(ctx.start.line) # type: ignore
        
    def exitPass(self, ctx: easmParser.PassContext) -> None:
        passing: str = str(self.terminals.pop())
        self.terminals.pop()  # 'pass' word

        passing = passing.lstrip('"').rstrip('"').replace('\\"', '"')

        if type(ctx.parentCtx) == easmParser.ExpressionContext:  # type: ignore
            self.expressions.append(passing)
        else:
            self.result.append(passing)
        for _ in range(1 + passing.count("\n")):
            self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitNewStat(self, ctx: easmParser.NewStatContext) -> None:
        name = str(self.terminals.pop())
        self.neededStructures.add(name)
        self.terminals.pop()  # 'local' modifier word or 'new' word (depends on context)
        if ctx.getChildCount() == 3:
            self.terminals.pop()  # 'new' word
            localID = self.ids.getRandomUId()
            self.expressions.append(
                f"{name}* {localID} = ({name}*)malloc(sizeof({name}));")
            self.terminals.append(f"(int64_t)({localID})")
            self.newLocalObjects.append(localID)
        else:
            self.terminals.append(f"(int64_t)({name}*)malloc(sizeof({name}))")

    def exitDelete(self, ctx: easmParser.DeleteContext) -> None:
        name = str(self.terminals.pop())
        self.terminals.pop()  # 'delete' word

        self.expressions.append(f"if ((void *){name} != NULL)")
        self.expressions.append(f"    free((void *){name});")
        for _ in range(2):
            self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitDot(self, ctx: easmParser.DotContext) -> None:
        param = str(self.terminals.pop())
        self.terminals.pop()  # '.' symbol
        name = str(self.terminals.pop())
        kind = str(self.terminals.pop())

        self.neededStructures.add(kind)

        self.expressions.append(f"if ((({kind} *){name}) != NULL)")
        self.terminals.append(f"(({kind}*){name})->{param}")
        self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitGetMem(self, ctx: easmParser.GetMemContext) -> None:
        self.terminals.pop()  # ']' symbol

        index = str(self.terminals.pop())  # maybe '[' symbol
        if index != '[':
            index = f" + {index}"
            self.terminals.pop()  # '[' symbol

        addr: str = str(self.terminals.pop()) + (index if index != "[" else '')

        kind: str = "int64_t"

        if hasattr(ctx.children[2], "getText"):  # type: ignore
            if ctx.children[2].getText() == "[":  # type: ignore
                kind = str(self.terminals.pop())

        self.terminals.append(f"*(({kind}*)({addr}))")

    def exitMove(self, ctx: easmParser.MoveContext) -> None:
        right = str(self.terminals.pop())
        self.terminals.pop()  # '->' symbol
        left = str(self.terminals.pop())

        self.expressions.append(f"{right} = {left};")
        self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitJump(self, ctx: easmParser.JumpContext) -> None:
        label = str(self.terminals.pop())

        self.neededLabels.add(label)

        if ctx.getChildCount() > 2:
            cond = str(self.terminals.pop())
            self.terminals.pop()  # 'if' word

            self.expressions.append(f"if ({cond}) goto {label};")
        else:
            self.expressions.append(f"goto {label};")
        
        self.expressionConnection.append(ctx.start.line) # type: ignore
        self.terminals.pop()  # 'jump' word

    def exitCondition(self, ctx: easmParser.ConditionContext) -> None:
        right = str(self.terminals.pop())
        action = str(self.terminals.pop())
        left = str(self.terminals.pop())

        if action == '=':
            action = '=='

        self.terminals.append(f"{left} {action} {right}")

    def exitLvalue(self, ctx: easmParser.LvalueContext) -> None:
        value = self.terminals.pop()
        if type(value) == str or str(value) in self.initializedLocals:
            self.terminals.append(value)
        else:
            self.terminals.append(value)
            self.initializedLocals.add(str(value))

    def exitBinaryOperator(self, ctx: easmParser.BinaryOperatorContext) -> None:
        second = str(self.terminals.pop())
        self.terminals.pop()  # ',' symbol
        first = str(self.terminals.pop())

        double: bool = False
        if ctx.getChildCount() == 5:
            kind = str(self.terminals.pop())
            if kind == "double":
                self.doubleResult = True
                double = True
        else:
            kind = "int64_t"

        if first in self.ids.decouplingUid:
            first: str = f"*({kind}*)(& {first})"
        if second in self.ids.decouplingUid:
            second: str = f"*({kind}*)(& {second})"

        action = str(self.terminals.pop())
        result: str = ""
        match action:
            case 'add':
                result = (f"({first}) + ({second})")
            case 'sub':
                result = (f"({first}) - ({second})")
            case 'mul':
                result = (f"({first}) * ({second})")
            case 'div':
                result = (f"({first}) / ({second})")
            case 'rem':
                if not "int" in kind:
                    self.handleException("RFV0", SharedExceptionLevel.Error, ctx,
                                         f"Attempt to get the reminder of two non-integral values: {first}, {second}")
                result = (f"({first}) % ({second})")
            case 'and':
                result = (f"({first}) & ({second})")
            case 'nand':
                result = (f"~(({first}) & ({second}))")
            case 'or':
                result = (f"({first}) | ({second})")
            case 'nor':
                result = (f"~(({first}) | ({second}))")
            case 'xor':
                result = (f"({first}) ^ ({second})")
            case 'xnor':
                result = (f"~(({first}) ^ ({second}))")
            case 'shr':
                if not "int" in kind:
                    self.handleException("SFV0", SharedExceptionLevel.Error, ctx,
                                         f"Attempt to shift with two non-integral values: {first}, {second}")
                result = (f"({first}) >> ({second})")
            case 'shl':
                if not "int" in kind:
                    self.handleException("SFV1", SharedExceptionLevel.Error, ctx,
                                         f"Attempt to shift with two non-integral values: {first}, {second}")
                result = (f"({first}) << ({second})")
            case _:
                result = (f"({first}) {action} ({second})")
        if double:
            self.expressions.append(f"dbres = {result};")
            self.terminals.append("*((int64_t*)&dbres)")
            self.expressionConnection.append(ctx.start.line) # type: ignore
        else:
            self.terminals.append(result)

    def exitInc(self, ctx: easmParser.IncContext) -> None:
        value = str(self.terminals.pop())
        self.terminals.pop()  # 'inc' word

        self.expressions.append(f"{value}++;")
        self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitDec(self, ctx: easmParser.DecContext) -> None:
        value = str(self.terminals.pop())
        self.terminals.pop()  # 'dec' word

        self.expressions.append(f"{value}--;")
        self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitNot(self, ctx: easmParser.NotContext) -> None:
        value = str(self.terminals.pop())
        self.terminals.pop()  # 'not' word

        self.terminals.append(f"~{value}")

    def exitPtr(self, ctx: easmParser.PtrContext) -> None:
        value = str(self.terminals.pop())
        self.terminals.pop()  # 'ptr' word

        self.terminals.append(f"(int64_t)(& {value})")

    def exitValueType(self, ctx: easmParser.ValueTypeContext) -> None:
        kind = str(self.terminals.pop())
        if kind == "string":
            self.terminals.append("const char*")
        elif kind == "int":
            self.terminals.append("int64_t")
        elif kind == "float":
            self.terminals.append("double")
        else:
            self.terminals.append(kind)

    def exitStacksize(self, ctx: easmParser.StacksizeContext) -> None:
        self.terminals.pop()  # 'ssize' word ('stack size' maybe)

        self.terminals.append("easm_ssize()")

    def exitPush(self, ctx: easmParser.PushContext) -> None:
        value = str(self.terminals.pop())
        self.terminals.pop()  # 'push' word

        self.expressions.append(f"easm_spush({value});")
        self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitPull(self, ctx: easmParser.PullContext) -> None:
        # or 'pull' word (depends on context)
        value = str(self.terminals.pop())

        if ctx.getChildCount() == 2:
            self.terminals.pop()  # 'pull' word
            self.expressions.append(f"{value} = easm_spull();")
        else:
            self.expressions.append("easm_spull();")
        self.expressionConnection.append(ctx.start.line) # type: ignore

    def exitCast(self, ctx: easmParser.CastContext) -> None:
        kind = str(self.terminals.pop())
        self.terminals.pop()  # 'as' word
        value = str(self.terminals.pop())

        self.terminals.append(f"*(({kind}*)(& {value}))")


class easm2cBuilder(SharedBuilder):

    def build(self) -> None:
        with open(join(self.folder, "CMakeLists.txt"), 'w') as cmakefile:
            cmakefile.write("cmake_minimum_required(VERSION 3.20)\n")
            cmakefile.write("set(CMAKE_MESSAGE_LOG_LEVEL WARNING)\n")
            cmakefile.write(f"project(easmProgram C)\n")
            cmakefile.write("add_executable(easmProgram EASMTranslated.c)")

        if not isdir(join(self.folder, "native_build")):
            mkdir(join(self.folder, "native_build"))

        from shutil import which

        cmakeAddr: str | None = which("cmake")

        if cmakeAddr == None:

            self.exceptions.append(
                SharedException(
                    "NCC0",
                    SharedExceptionLevel.Error,
                    0,  
                    0, 
                    "",
                    "To build the result you need cmake and at least one native C compiler to be installed."
                )
            )
            return

        from subprocess import Popen, PIPE, TimeoutExpired

        cmakeProcess = Popen([cmakeAddr, "../"],
                                cwd=join(self.folder, "native_build"), stdout=PIPE, stderr=PIPE)
        
        try:
            outs, errs = cmakeProcess.communicate(timeout=60)
        except TimeoutExpired:
            cmakeProcess.kill()
            outs, errs = cmakeProcess.communicate()

        if errs != b'':
            self.exceptions.append(
                SharedException(
                    "PGE0",
                    SharedExceptionLevel.Error,
                    0,
                    0,
                    "generated CMakeLists.txt file",
                    f"{errs.decode()}\n\33[91mPlease report the bug to the developer.\33[0m"
                )
            )
            return

        cmakeProcess = Popen([cmakeAddr, "--build", "."],
                                cwd=join(self.folder, "native_build"), stdout=PIPE)
        
        try:
            outs, _ = cmakeProcess.communicate(timeout=60)
        except TimeoutExpired:
            cmakeProcess.kill()
            outs, _ = cmakeProcess.communicate()

        from re import findall

        print(findall(r"EASMTranslated\.c\(\d+,\d+\): error \w+", outs.decode()))

        return

        if outs != b'':
            self.exceptions.append(
                SharedException(
                    "CTE0",
                    SharedExceptionLevel.Error,
                    0,
                    0,
                    "",
                    f"{outs.decode()}"
                )
            )
            return


class easm2cRunner(SharedRunner):

    def run(self) -> None:

        from subprocess import Popen
        Popen([join(self.outFolder, "native_build", "Debug", "easmProgram.exe")]).wait()

easm2c = SharedHandler(
    "easm2c",
    easm2cTranslator, 
    easm2cBuilder,
    easm2cRunner,
    easm2cRuntime,
    easm2cVersion
)
