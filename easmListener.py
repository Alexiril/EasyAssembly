# Generated from easm.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .easmParser import easmParser
else:
    from easmParser import easmParser

# This class defines a complete listener for a parse tree produced by easmParser.
class easmListener(ParseTreeListener):

    # Enter a parse tree produced by easmParser#program.
    def enterProgram(self, ctx:easmParser.ProgramContext):
        pass

    # Exit a parse tree produced by easmParser#program.
    def exitProgram(self, ctx:easmParser.ProgramContext):
        pass


    # Enter a parse tree produced by easmParser#structure.
    def enterStructure(self, ctx:easmParser.StructureContext):
        pass

    # Exit a parse tree produced by easmParser#structure.
    def exitStructure(self, ctx:easmParser.StructureContext):
        pass


    # Enter a parse tree produced by easmParser#function.
    def enterFunction(self, ctx:easmParser.FunctionContext):
        pass

    # Exit a parse tree produced by easmParser#function.
    def exitFunction(self, ctx:easmParser.FunctionContext):
        pass


    # Enter a parse tree produced by easmParser#importStat.
    def enterImportStat(self, ctx:easmParser.ImportStatContext):
        pass

    # Exit a parse tree produced by easmParser#importStat.
    def exitImportStat(self, ctx:easmParser.ImportStatContext):
        pass


    # Enter a parse tree produced by easmParser#expression.
    def enterExpression(self, ctx:easmParser.ExpressionContext):
        pass

    # Exit a parse tree produced by easmParser#expression.
    def exitExpression(self, ctx:easmParser.ExpressionContext):
        pass


    # Enter a parse tree produced by easmParser#pass.
    def enterPass(self, ctx:easmParser.PassContext):
        pass

    # Exit a parse tree produced by easmParser#pass.
    def exitPass(self, ctx:easmParser.PassContext):
        pass


    # Enter a parse tree produced by easmParser#delete.
    def enterDelete(self, ctx:easmParser.DeleteContext):
        pass

    # Exit a parse tree produced by easmParser#delete.
    def exitDelete(self, ctx:easmParser.DeleteContext):
        pass


    # Enter a parse tree produced by easmParser#jump.
    def enterJump(self, ctx:easmParser.JumpContext):
        pass

    # Exit a parse tree produced by easmParser#jump.
    def exitJump(self, ctx:easmParser.JumpContext):
        pass


    # Enter a parse tree produced by easmParser#label.
    def enterLabel(self, ctx:easmParser.LabelContext):
        pass

    # Exit a parse tree produced by easmParser#label.
    def exitLabel(self, ctx:easmParser.LabelContext):
        pass


    # Enter a parse tree produced by easmParser#move.
    def enterMove(self, ctx:easmParser.MoveContext):
        pass

    # Exit a parse tree produced by easmParser#move.
    def exitMove(self, ctx:easmParser.MoveContext):
        pass


    # Enter a parse tree produced by easmParser#push.
    def enterPush(self, ctx:easmParser.PushContext):
        pass

    # Exit a parse tree produced by easmParser#push.
    def exitPush(self, ctx:easmParser.PushContext):
        pass


    # Enter a parse tree produced by easmParser#pull.
    def enterPull(self, ctx:easmParser.PullContext):
        pass

    # Exit a parse tree produced by easmParser#pull.
    def exitPull(self, ctx:easmParser.PullContext):
        pass


    # Enter a parse tree produced by easmParser#condition.
    def enterCondition(self, ctx:easmParser.ConditionContext):
        pass

    # Exit a parse tree produced by easmParser#condition.
    def exitCondition(self, ctx:easmParser.ConditionContext):
        pass


    # Enter a parse tree produced by easmParser#inc.
    def enterInc(self, ctx:easmParser.IncContext):
        pass

    # Exit a parse tree produced by easmParser#inc.
    def exitInc(self, ctx:easmParser.IncContext):
        pass


    # Enter a parse tree produced by easmParser#dec.
    def enterDec(self, ctx:easmParser.DecContext):
        pass

    # Exit a parse tree produced by easmParser#dec.
    def exitDec(self, ctx:easmParser.DecContext):
        pass


    # Enter a parse tree produced by easmParser#rvalue.
    def enterRvalue(self, ctx:easmParser.RvalueContext):
        pass

    # Exit a parse tree produced by easmParser#rvalue.
    def exitRvalue(self, ctx:easmParser.RvalueContext):
        pass


    # Enter a parse tree produced by easmParser#newStat.
    def enterNewStat(self, ctx:easmParser.NewStatContext):
        pass

    # Exit a parse tree produced by easmParser#newStat.
    def exitNewStat(self, ctx:easmParser.NewStatContext):
        pass


    # Enter a parse tree produced by easmParser#call.
    def enterCall(self, ctx:easmParser.CallContext):
        pass

    # Exit a parse tree produced by easmParser#call.
    def exitCall(self, ctx:easmParser.CallContext):
        pass


    # Enter a parse tree produced by easmParser#array.
    def enterArray(self, ctx:easmParser.ArrayContext):
        pass

    # Exit a parse tree produced by easmParser#array.
    def exitArray(self, ctx:easmParser.ArrayContext):
        pass


    # Enter a parse tree produced by easmParser#ptr.
    def enterPtr(self, ctx:easmParser.PtrContext):
        pass

    # Exit a parse tree produced by easmParser#ptr.
    def exitPtr(self, ctx:easmParser.PtrContext):
        pass


    # Enter a parse tree produced by easmParser#not.
    def enterNot(self, ctx:easmParser.NotContext):
        pass

    # Exit a parse tree produced by easmParser#not.
    def exitNot(self, ctx:easmParser.NotContext):
        pass


    # Enter a parse tree produced by easmParser#stacksize.
    def enterStacksize(self, ctx:easmParser.StacksizeContext):
        pass

    # Exit a parse tree produced by easmParser#stacksize.
    def exitStacksize(self, ctx:easmParser.StacksizeContext):
        pass


    # Enter a parse tree produced by easmParser#binaryOperator.
    def enterBinaryOperator(self, ctx:easmParser.BinaryOperatorContext):
        pass

    # Exit a parse tree produced by easmParser#binaryOperator.
    def exitBinaryOperator(self, ctx:easmParser.BinaryOperatorContext):
        pass


    # Enter a parse tree produced by easmParser#cvalue.
    def enterCvalue(self, ctx:easmParser.CvalueContext):
        pass

    # Exit a parse tree produced by easmParser#cvalue.
    def exitCvalue(self, ctx:easmParser.CvalueContext):
        pass


    # Enter a parse tree produced by easmParser#lvalue.
    def enterLvalue(self, ctx:easmParser.LvalueContext):
        pass

    # Exit a parse tree produced by easmParser#lvalue.
    def exitLvalue(self, ctx:easmParser.LvalueContext):
        pass


    # Enter a parse tree produced by easmParser#cast.
    def enterCast(self, ctx:easmParser.CastContext):
        pass

    # Exit a parse tree produced by easmParser#cast.
    def exitCast(self, ctx:easmParser.CastContext):
        pass


    # Enter a parse tree produced by easmParser#dot.
    def enterDot(self, ctx:easmParser.DotContext):
        pass

    # Exit a parse tree produced by easmParser#dot.
    def exitDot(self, ctx:easmParser.DotContext):
        pass


    # Enter a parse tree produced by easmParser#getMem.
    def enterGetMem(self, ctx:easmParser.GetMemContext):
        pass

    # Exit a parse tree produced by easmParser#getMem.
    def exitGetMem(self, ctx:easmParser.GetMemContext):
        pass


    # Enter a parse tree produced by easmParser#dataTypeDeclaration.
    def enterDataTypeDeclaration(self, ctx:easmParser.DataTypeDeclarationContext):
        pass

    # Exit a parse tree produced by easmParser#dataTypeDeclaration.
    def exitDataTypeDeclaration(self, ctx:easmParser.DataTypeDeclarationContext):
        pass


    # Enter a parse tree produced by easmParser#valueType.
    def enterValueType(self, ctx:easmParser.ValueTypeContext):
        pass

    # Exit a parse tree produced by easmParser#valueType.
    def exitValueType(self, ctx:easmParser.ValueTypeContext):
        pass



del easmParser