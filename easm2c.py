from os import mkdir
from os.path import isdir, join
from random import randint
from struct import pack, unpack

from antlr4.Parser import ParserRuleContext  # type: ignore

from easmLexer import easmLexer
from easmListener import easmListener
from easmParser import ErrorNode, TerminalNode, easmParser
from unifiedException import UnifiedException, UnifiedExceptionLevel

easm2cVersion: tuple[int, int, int] = (0, 2, 0)


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
"""


class easm2cTranslator(easmListener):

    def __init__(self, filecode: str, filename: str) -> None:
        super().__init__()
        self.filecode = filecode
        self.filename = filename
        self.uids: list[str] = list()
        self.exceptions: list[UnifiedException] = list()
        self.terminals: list[TerminalNode | str] = list()
        self.expressions: list[str] = []
        self.newLocalObjects: list[str] = list()
        self.initializedLocals: set[str] = set()
        self.doubleResult: bool = False
        self.functions: set[str] = set()
        self.structures: set[str] = set()
        self.neededStructures: set[str] = set()
        self.labels: dict[str, set[str]] = dict()
        self.labelsInFunction: set[str] = set()
        self.neededLabels: set[str] = set()
        self.decouplingId: dict[str, str] = dict()
        self.decouplingUid: dict[str, str] = dict()
        self.imports: set[str] = set()
        self.result: list[str] = list()

    def getRuntime(self) -> str:
        return """
#ifndef __EASM_RUNTIME
#define __EASM_RUNTIME
#include <stdint.h>
#include <malloc.h>
typedef struct stackNode { int64_t* data; struct stackNode* next; } stackNode;
stackNode* stackTop = NULL;
int64_t __easm_ssize = 0;
uint64_t easm_ssize() {
    return __easm_ssize;
}
int64_t easm_spull() {
    if (stackTop == NULL)
        return 0;
    stackNode* temp = stackTop;
    int64_t* data = temp->data;
    stackTop = stackTop->next;
    free(temp);
    return data;
}
void easm_spush(uint64_t num) {
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

    def __str__(self) -> str:
        return self.getRuntime() + "\n".join(self.result)

    def getRandomUId(self) -> str:
        result = '_'
        while result in self.uids or result == '_':
            result: str = '_' + hex(randint(0, 0xFFFFFF))
        self.uids.append(result)
        return result

    def decoupleId(self, id: str) -> str:
        if id in self.decouplingId:
            return self.decouplingId[id]
        uid = self.getRandomUId()
        self.decouplingId[id] = uid
        self.decouplingUid[uid] = id
        return uid

    def handleException(self, code: str, level: UnifiedExceptionLevel, ctx: TerminalNode | ParserRuleContext, msg: str) -> None:
        line: int = 0
        column: int = 0

        if type(ctx) == TerminalNode:
            line = ctx.getSymbol().line  # type: ignore
            column = ctx.getSymbol().column  # type: ignore
        elif type(ctx) == ParserRuleContext:
            line = ctx.start.line  # type: ignore
            column = ctx.start.column  # type: ignore

        self.exceptions.append(
            UnifiedException(
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
            UnifiedExceptionLevel.Error,
            node,
            f"Unexpected expression: \"{node}\""
        )

    def visitTerminal(self, node: TerminalNode | str) -> None:
        if node.getSymbol().type == easmLexer.FConst:  # type: ignore
            packed = pack('d', float(node.getText()))  # type: ignore
            node = hex(unpack('Q', packed)[0])
        elif node.getSymbol().type == easmLexer.Id:  # type: ignore
            node.getSymbol().text = self.decoupleId(node.getText())  # type: ignore
        self.terminals.append(node)

    def enterProgram(self, ctx: easmParser.ProgramContext) -> None:
        self.result.append(f"// File: '{self.filename}'")
        self.result.append("// < Auto generated using EASM2C >")
        self.result.append(f"#ifndef {self.filecode}_H")
        self.result.append(f"#define {self.filecode}_H\n")

    def exitProgram(self, ctx: easmParser.ProgramContext) -> None:
        self.result.append("#endif")
        self.result.append("// < Auto generated using EASM2C >\n")

    def exitFunction(self, ctx: easmParser.FunctionContext) -> None:
        functionName: str = str(self.terminals.pop())
        self.terminals.pop()  # 'func' word

        if functionName in self.functions:
            self.handleException("FSN0", UnifiedExceptionLevel.Error, ctx,
                                 f"Functions cannot have the same name: {self.decouplingUid[functionName]}")

        self.functions.add(functionName)

        for initLocal in self.initializedLocals:
            self.expressions.insert(
                0, f"int64_t {initLocal} = 0; // {self.decouplingUid[initLocal]}")

        if self.doubleResult:
            self.expressions.insert(0, "double dbres = 0;")
        self.doubleResult = False

        for localObject in self.newLocalObjects:
            self.expressions.append(f"if ((void *){localObject} != NULL)")
            self.expressions.append(f"    free((void *){localObject});")
        self.newLocalObjects.clear()

        self.expressions.append("return;")
        expressions: str = '\n    '.join(self.expressions)

        funcInC: str = f"void {functionName} () {{\n    {expressions}  \n}}\n"

        self.expressions.clear()

        self.labels[functionName] = self.labelsInFunction

        for label in self.neededLabels:
            if not label in self.labelsInFunction:
                self.handleException("LFN0", UnifiedExceptionLevel.Error, ctx,
                                     f"Label is not found in the function: {self.decouplingUid[label]}")

        self.labelsInFunction.clear()
        self.neededLabels.clear()
        self.initializedLocals.clear()

        self.result.append(
            f"// {functionName} is {self.decouplingUid[functionName]}")

        self.result.append(funcInC)

        if self.decouplingUid[functionName] == "main":
            self.result.append("int main() {")
            self.result.append(f"    {functionName}();")
            self.result.append("    return 0;")
            self.result.append("}")

    def exitImportStat(self, ctx: easmParser.ImportStatContext) -> None:
        value = str(self.terminals.pop())
        self.terminals.pop()  # 'native' or 'import' word (depends on context)

        if ctx.getChildCount() == 3:
            self.terminals.pop()  # 'import' word
            self.result.append(f"#include {value}")
        else:
            self.imports.add(value.replace('"', ''))

    def exitStructure(self, ctx: easmParser.StructureContext) -> None:
        elements: list[str] = [str(self.terminals.pop())
                               for _ in range(ctx.getChildCount() - 2)]
        structureName = str(self.terminals.pop())
        self.terminals.pop()  # 'struct' word

        if structureName in self.structures:
            self.handleException("SSN0", UnifiedExceptionLevel.Error, ctx,
                                 f"Structures cannot have the same name: {structureName}")

        self.structures.add(structureName)
        stringInside: str = ";\n    ".join(elements[::-1]) + ";"

        self.result.append(
            f"// {structureName} is {self.decouplingUid[structureName]}")
        self.result.append(f"typedef struct {structureName} {{")
        self.result.append(f"    {stringInside}")
        self.result.append(f"}} {structureName};\n")

    def exitDataTypeDeclaration(self, ctx: easmParser.DataTypeDeclarationContext) -> None:
        value = str(self.terminals.pop())
        kind = str(self.terminals.pop())
        self.terminals.append(f"{kind} {value}")

    def exitLabel(self, ctx: easmParser.LabelContext) -> None:
        self.terminals.pop()  # ':' symbol
        label = str(self.terminals.pop())

        if label in self.labelsInFunction:
            self.handleException("LSN0", UnifiedExceptionLevel.Error, ctx,
                                 f"Labels inside one function cannot have the same name: {label}")
        self.labelsInFunction.add(label)

        self.expressions.append(f"{label}:")

    def exitCall(self, ctx: easmParser.CallContext) -> None:
        funcToCall = str(self.terminals.pop())
        self.terminals.pop()  # 'call' word

        self.expressions.append(f"{funcToCall} ();")

    def exitInvoke(self, ctx: easmParser.InvokeContext) -> None:
        params_count = ctx.getChildCount() - 4
        self.terminals.pop()  # ')' symbol
        params: list[str] = list()
        for i in range(params_count):
            value = str(self.terminals.pop())
            if i % 2 == 0:
                params.append(value)
        self.terminals.pop()  # '(' symbol
        funcToInvoke = str(self.terminals.pop())
        self.terminals.pop()  # 'invoke' word

        cstring = f"{self.decouplingUid[funcToInvoke]}({','.join(params[::-1])})"

        if type(ctx.parentCtx) == easmParser.RvalueContext:  # type: ignore
            self.terminals.append(cstring)
        else:
            self.expressions.append(cstring + ";")

    def exitPass(self, ctx: easmParser.PassContext) -> None:
        passing: str = str(self.terminals.pop())
        self.terminals.pop()  # 'pass' word

        passing = passing.lstrip('"').rstrip('"').replace('\\"', '"')

        if type(ctx.parentCtx) == easmParser.ExpressionContext:  # type: ignore
            self.expressions.append(passing)
        else:
            self.result.append(passing)

    def exitNewStat(self, ctx: easmParser.NewStatContext) -> None:
        name = str(self.terminals.pop())
        self.neededStructures.add(name)
        self.terminals.pop()  # 'local' modifier word or 'new' word (depends on context)
        if ctx.getChildCount() == 3:
            self.terminals.pop()  # 'new' word
            localID = self.getRandomUId()
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

    def exitDot(self, ctx: easmParser.DotContext) -> None:
        param = str(self.terminals.pop())
        self.terminals.pop()  # '.' symbol
        name = str(self.terminals.pop())
        kind = str(self.terminals.pop())

        self.neededStructures.add(kind)

        self.expressions.append(f"if ((({kind} *){name}) != NULL)")
        self.terminals.append(f"(({kind}*){name})->{param}")

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

    def exitJump(self, ctx: easmParser.JumpContext) -> None:
        label = str(self.terminals.pop())

        self.neededLabels.add(label)

        if ctx.getChildCount() > 2:
            cond = str(self.terminals.pop())
            self.terminals.pop()  # 'if' word

            self.expressions.append(f"if ({cond}) goto {label};")
        else:
            self.expressions.append(f"goto {label};")

        self.terminals.pop()  # 'jump' word

    def exitCondition(self, ctx: easmParser.ConditionContext) -> None:
        right = str(self.terminals.pop())
        action = str(self.terminals.pop())
        left = str(self.terminals.pop())

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

        if first in self.decouplingUid:
            first: str = f"*({kind}*)(& {first})"
        if second in self.decouplingUid:
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
                    self.handleException("RFV0", UnifiedExceptionLevel.Error, ctx,
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
                    self.handleException("SFV0", UnifiedExceptionLevel.Error, ctx,
                                         f"Attempt to shift with two non-integral values: {first}, {second}")
                result = (f"({first}) >> ({second})")
            case 'shl':
                if not "int" in kind:
                    self.handleException("SFV1", UnifiedExceptionLevel.Error, ctx,
                                         f"Attempt to shift with two non-integral values: {first}, {second}")
                result = (f"({first}) << ({second})")
            case _:
                result = (f"({first}) {action} ({second})")
        if double:
            self.expressions.append(f"dbres = {result};")
            self.terminals.append("*((int64_t*)&dbres)")
        else:
            self.terminals.append(result)

    def exitInc(self, ctx: easmParser.IncContext) -> None:
        value = str(self.terminals.pop())
        self.terminals.pop()  # 'inc' word

        self.expressions.append(f"{value}++;")

    def exitDec(self, ctx: easmParser.DecContext) -> None:
        value = str(self.terminals.pop())
        self.terminals.pop()  # 'dec' word

        self.expressions.append(f"{value}--;")

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

    def exitPull(self, ctx: easmParser.PullContext) -> None:
        # or 'pull' word (depends on context)
        value = str(self.terminals.pop())

        if ctx.getChildCount() == 2:
            self.terminals.pop()  # 'pull' word
            self.expressions.append(f"{value} = easm_spull();")
        else:
            self.expressions.append("easm_spull();")

    def exitCast(self, ctx: easmParser.CastContext) -> None:
        kind = str(self.terminals.pop())
        self.terminals.pop() # 'as' word
        value = str(self.terminals.pop())

        self.terminals.append(f"*(({kind}*)(& {value}))")

class easm2cBuilder:

    def __init__(self, folder: str, code: str) -> None:
        self.exceptions: list[UnifiedException] = list()
        self.code = code
        self.folder = folder

    def build(self) -> None:
        with open(join(self.folder, "EASMTranslated.c"), 'w') as cfile:
            cfile.write(self.code)

        with open(join(self.folder, "CMakeLists.txt"), 'w') as cmakefile:
            cmakefile.write("cmake_minimum_required(VERSION 3.20)\n")
            cmakefile.write("set(CMAKE_MESSAGE_LOG_LEVEL WARNING)\n")
            cmakefile.write(f"project(easmProgram C)\n")
            cmakefile.write("add_executable(easmProgram EASMTranslated.c)")

        if not isdir(join(self.folder, "native_build")):
            mkdir(join(self.folder, "native_build"))

        from shutil import which

        cmakeAddr: str | None = which("cmake")

        if cmakeAddr != None:

            from subprocess import Popen

            cmakeProcess = Popen([cmakeAddr, "../"],
                                 cwd=join(self.folder, "native_build"))
            cmakeProcess.wait()

            cmakeProcess = Popen([cmakeAddr, "--build", "."],
                                 cwd=join(self.folder, "native_build"))
            cmakeProcess.wait()

        else:

            self.exceptions.append(
                UnifiedException(
                    "NNN",
                    UnifiedExceptionLevel.Error,
                    0,  # type: ignore
                    0,  # type: ignore
                    "",
                    "To build the result you need cmake and one native C compiler to be installed."
                )
            )
