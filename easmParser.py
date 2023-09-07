# Generated from easm.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,252,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,1,0,1,0,5,0,66,8,0,10,
        0,12,0,69,9,0,1,0,1,0,1,1,1,1,1,1,4,1,76,8,1,11,1,12,1,77,1,2,1,
        2,1,2,5,2,83,8,2,10,2,12,2,86,9,2,1,3,1,3,3,3,90,8,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,105,8,4,1,5,1,5,1,5,
        1,6,1,6,1,6,1,7,1,7,1,7,3,7,116,8,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,3,12,135,8,12,1,
        13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,146,8,14,1,15,1,
        15,1,15,1,15,1,15,3,15,153,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,3,16,163,8,16,1,17,1,17,3,17,167,8,17,1,17,1,17,1,18,1,18,
        1,18,3,18,174,8,18,1,19,1,19,1,19,1,19,1,19,3,19,181,8,19,1,20,1,
        20,1,21,1,21,1,21,1,21,1,21,1,21,5,21,191,8,21,10,21,12,21,194,9,
        21,3,21,196,8,21,1,21,1,21,1,22,1,22,3,22,202,8,22,1,22,1,22,3,22,
        206,8,22,1,22,1,22,1,22,3,22,211,8,22,1,22,1,22,1,23,1,23,1,23,1,
        23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,3,24,226,8,24,1,25,1,25,1,
        25,3,25,231,8,25,1,26,1,26,1,26,1,26,3,26,237,8,26,1,27,1,27,1,27,
        1,27,1,27,1,28,1,28,3,28,246,8,28,1,28,1,28,1,29,1,29,1,29,0,0,30,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,0,4,1,0,14,19,1,0,26,27,1,0,34,46,1,0,49,51,
        273,0,60,1,0,0,0,2,72,1,0,0,0,4,79,1,0,0,0,6,87,1,0,0,0,8,104,1,
        0,0,0,10,106,1,0,0,0,12,109,1,0,0,0,14,112,1,0,0,0,16,119,1,0,0,
        0,18,122,1,0,0,0,20,125,1,0,0,0,22,129,1,0,0,0,24,132,1,0,0,0,26,
        136,1,0,0,0,28,140,1,0,0,0,30,147,1,0,0,0,32,162,1,0,0,0,34,164,
        1,0,0,0,36,170,1,0,0,0,38,175,1,0,0,0,40,182,1,0,0,0,42,184,1,0,
        0,0,44,201,1,0,0,0,46,214,1,0,0,0,48,225,1,0,0,0,50,230,1,0,0,0,
        52,232,1,0,0,0,54,238,1,0,0,0,56,245,1,0,0,0,58,249,1,0,0,0,60,67,
        5,52,0,0,61,66,3,6,3,0,62,66,3,4,2,0,63,66,3,2,1,0,64,66,3,10,5,
        0,65,61,1,0,0,0,65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,69,
        1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,
        70,71,5,0,0,1,71,1,1,0,0,0,72,73,5,1,0,0,73,75,5,53,0,0,74,76,3,
        56,28,0,75,74,1,0,0,0,76,77,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,
        78,3,1,0,0,0,79,80,5,2,0,0,80,84,5,53,0,0,81,83,3,8,4,0,82,81,1,
        0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,5,1,0,0,0,86,
        84,1,0,0,0,87,89,5,3,0,0,88,90,5,4,0,0,89,88,1,0,0,0,89,90,1,0,0,
        0,90,91,1,0,0,0,91,92,5,57,0,0,92,7,1,0,0,0,93,105,3,10,5,0,94,105,
        3,12,6,0,95,105,3,14,7,0,96,105,3,16,8,0,97,105,3,18,9,0,98,105,
        3,20,10,0,99,105,3,22,11,0,100,105,3,24,12,0,101,105,3,28,14,0,102,
        105,3,30,15,0,103,105,3,42,21,0,104,93,1,0,0,0,104,94,1,0,0,0,104,
        95,1,0,0,0,104,96,1,0,0,0,104,97,1,0,0,0,104,98,1,0,0,0,104,99,1,
        0,0,0,104,100,1,0,0,0,104,101,1,0,0,0,104,102,1,0,0,0,104,103,1,
        0,0,0,105,9,1,0,0,0,106,107,5,5,0,0,107,108,5,57,0,0,108,11,1,0,
        0,0,109,110,5,6,0,0,110,111,5,53,0,0,111,13,1,0,0,0,112,115,5,7,
        0,0,113,114,5,8,0,0,114,116,3,26,13,0,115,113,1,0,0,0,115,116,1,
        0,0,0,116,117,1,0,0,0,117,118,5,53,0,0,118,15,1,0,0,0,119,120,5,
        53,0,0,120,121,5,9,0,0,121,17,1,0,0,0,122,123,5,10,0,0,123,124,5,
        53,0,0,124,19,1,0,0,0,125,126,3,32,16,0,126,127,5,11,0,0,127,128,
        3,50,25,0,128,21,1,0,0,0,129,130,5,12,0,0,130,131,3,48,24,0,131,
        23,1,0,0,0,132,134,5,13,0,0,133,135,3,50,25,0,134,133,1,0,0,0,134,
        135,1,0,0,0,135,25,1,0,0,0,136,137,3,48,24,0,137,138,7,0,0,0,138,
        139,3,48,24,0,139,27,1,0,0,0,140,145,5,20,0,0,141,146,3,50,25,0,
        142,146,5,54,0,0,143,146,5,55,0,0,144,146,5,56,0,0,145,141,1,0,0,
        0,145,142,1,0,0,0,145,143,1,0,0,0,145,144,1,0,0,0,146,29,1,0,0,0,
        147,152,5,21,0,0,148,153,3,50,25,0,149,153,5,54,0,0,150,153,5,55,
        0,0,151,153,5,56,0,0,152,148,1,0,0,0,152,149,1,0,0,0,152,150,1,0,
        0,0,152,151,1,0,0,0,153,31,1,0,0,0,154,163,3,34,17,0,155,163,3,40,
        20,0,156,163,3,42,21,0,157,163,3,44,22,0,158,163,3,36,18,0,159,163,
        3,38,19,0,160,163,3,46,23,0,161,163,3,48,24,0,162,154,1,0,0,0,162,
        155,1,0,0,0,162,156,1,0,0,0,162,157,1,0,0,0,162,158,1,0,0,0,162,
        159,1,0,0,0,162,160,1,0,0,0,162,161,1,0,0,0,163,33,1,0,0,0,164,166,
        5,22,0,0,165,167,5,23,0,0,166,165,1,0,0,0,166,167,1,0,0,0,167,168,
        1,0,0,0,168,169,5,53,0,0,169,35,1,0,0,0,170,173,5,24,0,0,171,174,
        3,50,25,0,172,174,5,57,0,0,173,171,1,0,0,0,173,172,1,0,0,0,174,37,
        1,0,0,0,175,180,5,25,0,0,176,181,3,50,25,0,177,181,5,54,0,0,178,
        181,5,55,0,0,179,181,5,56,0,0,180,176,1,0,0,0,180,177,1,0,0,0,180,
        178,1,0,0,0,180,179,1,0,0,0,181,39,1,0,0,0,182,183,7,1,0,0,183,41,
        1,0,0,0,184,185,5,28,0,0,185,186,5,53,0,0,186,195,5,29,0,0,187,192,
        3,48,24,0,188,189,5,30,0,0,189,191,3,48,24,0,190,188,1,0,0,0,191,
        194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,196,1,0,0,0,194,
        192,1,0,0,0,195,187,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,
        198,5,31,0,0,198,43,1,0,0,0,199,202,5,53,0,0,200,202,3,58,29,0,201,
        199,1,0,0,0,201,200,1,0,0,0,201,202,1,0,0,0,202,205,1,0,0,0,203,
        206,3,50,25,0,204,206,5,54,0,0,205,203,1,0,0,0,205,204,1,0,0,0,206,
        207,1,0,0,0,207,210,5,32,0,0,208,211,3,50,25,0,209,211,5,54,0,0,
        210,208,1,0,0,0,210,209,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,
        212,213,5,33,0,0,213,45,1,0,0,0,214,215,7,2,0,0,215,216,3,58,29,
        0,216,217,3,48,24,0,217,218,5,30,0,0,218,219,3,48,24,0,219,47,1,
        0,0,0,220,226,3,50,25,0,221,226,5,54,0,0,222,226,5,55,0,0,223,226,
        5,56,0,0,224,226,5,57,0,0,225,220,1,0,0,0,225,221,1,0,0,0,225,222,
        1,0,0,0,225,223,1,0,0,0,225,224,1,0,0,0,226,49,1,0,0,0,227,231,5,
        53,0,0,228,231,3,54,27,0,229,231,3,52,26,0,230,227,1,0,0,0,230,228,
        1,0,0,0,230,229,1,0,0,0,231,51,1,0,0,0,232,233,5,53,0,0,233,236,
        5,47,0,0,234,237,5,53,0,0,235,237,3,58,29,0,236,234,1,0,0,0,236,
        235,1,0,0,0,237,53,1,0,0,0,238,239,5,53,0,0,239,240,5,53,0,0,240,
        241,5,48,0,0,241,242,5,53,0,0,242,55,1,0,0,0,243,246,5,53,0,0,244,
        246,3,58,29,0,245,243,1,0,0,0,245,244,1,0,0,0,246,247,1,0,0,0,247,
        248,5,53,0,0,248,57,1,0,0,0,249,250,7,3,0,0,250,59,1,0,0,0,23,65,
        67,77,84,89,104,115,134,145,152,162,166,173,180,192,195,201,205,
        210,225,230,236,245
    ]

class easmParser ( Parser ):

    grammarFileName = "easm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'func'", "'import'", "'native'", 
                     "'pass'", "'delete'", "'jump'", "'if'", "':'", "'call'", 
                     "'->'", "'push'", "'pull'", "'='", "'!='", "'>'", "'<'", 
                     "'>='", "'<='", "'inc'", "'dec'", "'new'", "'local'", 
                     "'ptr'", "'not'", "'stack size'", "'ssize'", "'invoke'", 
                     "'('", "','", "')'", "'['", "']'", "'and'", "'or'", 
                     "'xor'", "'nor'", "'nand'", "'xnor'", "'add'", "'sub'", 
                     "'mul'", "'div'", "'rem'", "'shr'", "'shl'", "'as'", 
                     "'.'", "'int'", "'float'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Pony", "Id", "IConst", "FConst", "CConst", "SConst", 
                      "Whitespace", "Newline", "BlockComment", "LineComment" ]

    RULE_program = 0
    RULE_structure = 1
    RULE_function = 2
    RULE_importStat = 3
    RULE_expression = 4
    RULE_pass = 5
    RULE_delete = 6
    RULE_jump = 7
    RULE_label = 8
    RULE_call = 9
    RULE_move = 10
    RULE_push = 11
    RULE_pull = 12
    RULE_condition = 13
    RULE_inc = 14
    RULE_dec = 15
    RULE_rvalue = 16
    RULE_newStat = 17
    RULE_ptr = 18
    RULE_not = 19
    RULE_stacksize = 20
    RULE_invoke = 21
    RULE_getMem = 22
    RULE_binaryOperator = 23
    RULE_cvalue = 24
    RULE_lvalue = 25
    RULE_cast = 26
    RULE_dot = 27
    RULE_dataTypeDeclaration = 28
    RULE_valueType = 29

    ruleNames =  [ "program", "structure", "function", "importStat", "expression", 
                   "pass", "delete", "jump", "label", "call", "move", "push", 
                   "pull", "condition", "inc", "dec", "rvalue", "newStat", 
                   "ptr", "not", "stacksize", "invoke", "getMem", "binaryOperator", 
                   "cvalue", "lvalue", "cast", "dot", "dataTypeDeclaration", 
                   "valueType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    Pony=52
    Id=53
    IConst=54
    FConst=55
    CConst=56
    SConst=57
    Whitespace=58
    Newline=59
    BlockComment=60
    LineComment=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Pony(self):
            return self.getToken(easmParser.Pony, 0)

        def EOF(self):
            return self.getToken(easmParser.EOF, 0)

        def importStat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.ImportStatContext)
            else:
                return self.getTypedRuleContext(easmParser.ImportStatContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.FunctionContext)
            else:
                return self.getTypedRuleContext(easmParser.FunctionContext,i)


        def structure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.StructureContext)
            else:
                return self.getTypedRuleContext(easmParser.StructureContext,i)


        def pass_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.PassContext)
            else:
                return self.getTypedRuleContext(easmParser.PassContext,i)


        def getRuleIndex(self):
            return easmParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = easmParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(easmParser.Pony)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 46) != 0):
                self.state = 65
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 61
                    self.importStat()
                    pass
                elif token in [2]:
                    self.state = 62
                    self.function()
                    pass
                elif token in [1]:
                    self.state = 63
                    self.structure()
                    pass
                elif token in [5]:
                    self.state = 64
                    self.pass_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(easmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def dataTypeDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.DataTypeDeclarationContext)
            else:
                return self.getTypedRuleContext(easmParser.DataTypeDeclarationContext,i)


        def getRuleIndex(self):
            return easmParser.RULE_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructure" ):
                listener.enterStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructure" ):
                listener.exitStructure(self)




    def structure(self):

        localctx = easmParser.StructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(easmParser.T__0)
            self.state = 73
            self.match(easmParser.Id)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.dataTypeDeclaration()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12947848928690176) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(easmParser.ExpressionContext,i)


        def getRuleIndex(self):
            return easmParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = easmParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(easmParser.T__1)
            self.state = 80
            self.match(easmParser.Id)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self.expression() 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SConst(self):
            return self.getToken(easmParser.SConst, 0)

        def getRuleIndex(self):
            return easmParser.RULE_importStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStat" ):
                listener.enterImportStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStat" ):
                listener.exitImportStat(self)




    def importStat(self):

        localctx = easmParser.ImportStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_importStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(easmParser.T__2)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 88
                self.match(easmParser.T__3)


            self.state = 91
            self.match(easmParser.SConst)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pass_(self):
            return self.getTypedRuleContext(easmParser.PassContext,0)


        def delete(self):
            return self.getTypedRuleContext(easmParser.DeleteContext,0)


        def jump(self):
            return self.getTypedRuleContext(easmParser.JumpContext,0)


        def label(self):
            return self.getTypedRuleContext(easmParser.LabelContext,0)


        def call(self):
            return self.getTypedRuleContext(easmParser.CallContext,0)


        def move(self):
            return self.getTypedRuleContext(easmParser.MoveContext,0)


        def push(self):
            return self.getTypedRuleContext(easmParser.PushContext,0)


        def pull(self):
            return self.getTypedRuleContext(easmParser.PullContext,0)


        def inc(self):
            return self.getTypedRuleContext(easmParser.IncContext,0)


        def dec(self):
            return self.getTypedRuleContext(easmParser.DecContext,0)


        def invoke(self):
            return self.getTypedRuleContext(easmParser.InvokeContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = easmParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.pass_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.delete()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.jump()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.label()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 97
                self.call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 98
                self.move()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 99
                self.push()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 100
                self.pull()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 101
                self.inc()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 102
                self.dec()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 103
                self.invoke()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SConst(self):
            return self.getToken(easmParser.SConst, 0)

        def getRuleIndex(self):
            return easmParser.RULE_pass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPass" ):
                listener.enterPass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPass" ):
                listener.exitPass(self)




    def pass_(self):

        localctx = easmParser.PassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(easmParser.T__4)
            self.state = 107
            self.match(easmParser.SConst)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def getRuleIndex(self):
            return easmParser.RULE_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete" ):
                listener.enterDelete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete" ):
                listener.exitDelete(self)




    def delete(self):

        localctx = easmParser.DeleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(easmParser.T__5)
            self.state = 110
            self.match(easmParser.Id)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def condition(self):
            return self.getTypedRuleContext(easmParser.ConditionContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_jump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump" ):
                listener.enterJump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump" ):
                listener.exitJump(self)




    def jump(self):

        localctx = easmParser.JumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_jump)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(easmParser.T__6)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 113
                self.match(easmParser.T__7)
                self.state = 114
                self.condition()


            self.state = 117
            self.match(easmParser.Id)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def getRuleIndex(self):
            return easmParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = easmParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(easmParser.Id)
            self.state = 120
            self.match(easmParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def getRuleIndex(self):
            return easmParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = easmParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(easmParser.T__9)
            self.state = 123
            self.match(easmParser.Id)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(easmParser.RvalueContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(easmParser.LvalueContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_move

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove" ):
                listener.enterMove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove" ):
                listener.exitMove(self)




    def move(self):

        localctx = easmParser.MoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_move)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.rvalue()
            self.state = 126
            self.match(easmParser.T__10)
            self.state = 127
            self.lvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PushContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cvalue(self):
            return self.getTypedRuleContext(easmParser.CvalueContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_push

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPush" ):
                listener.enterPush(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPush" ):
                listener.exitPush(self)




    def push(self):

        localctx = easmParser.PushContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_push)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(easmParser.T__11)
            self.state = 130
            self.cvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(easmParser.LvalueContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_pull

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPull" ):
                listener.enterPull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPull" ):
                listener.exitPull(self)




    def pull(self):

        localctx = easmParser.PullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_pull)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(easmParser.T__12)
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 133
                self.lvalue()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.CvalueContext)
            else:
                return self.getTypedRuleContext(easmParser.CvalueContext,i)


        def getRuleIndex(self):
            return easmParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = easmParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.cvalue()
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 138
            self.cvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(easmParser.LvalueContext,0)


        def IConst(self):
            return self.getToken(easmParser.IConst, 0)

        def FConst(self):
            return self.getToken(easmParser.FConst, 0)

        def CConst(self):
            return self.getToken(easmParser.CConst, 0)

        def getRuleIndex(self):
            return easmParser.RULE_inc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInc" ):
                listener.enterInc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInc" ):
                listener.exitInc(self)




    def inc(self):

        localctx = easmParser.IncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_inc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(easmParser.T__19)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 141
                self.lvalue()
                pass
            elif token in [54]:
                self.state = 142
                self.match(easmParser.IConst)
                pass
            elif token in [55]:
                self.state = 143
                self.match(easmParser.FConst)
                pass
            elif token in [56]:
                self.state = 144
                self.match(easmParser.CConst)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(easmParser.LvalueContext,0)


        def IConst(self):
            return self.getToken(easmParser.IConst, 0)

        def FConst(self):
            return self.getToken(easmParser.FConst, 0)

        def CConst(self):
            return self.getToken(easmParser.CConst, 0)

        def getRuleIndex(self):
            return easmParser.RULE_dec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec" ):
                listener.enterDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec" ):
                listener.exitDec(self)




    def dec(self):

        localctx = easmParser.DecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(easmParser.T__20)
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 148
                self.lvalue()
                pass
            elif token in [54]:
                self.state = 149
                self.match(easmParser.IConst)
                pass
            elif token in [55]:
                self.state = 150
                self.match(easmParser.FConst)
                pass
            elif token in [56]:
                self.state = 151
                self.match(easmParser.CConst)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newStat(self):
            return self.getTypedRuleContext(easmParser.NewStatContext,0)


        def stacksize(self):
            return self.getTypedRuleContext(easmParser.StacksizeContext,0)


        def invoke(self):
            return self.getTypedRuleContext(easmParser.InvokeContext,0)


        def getMem(self):
            return self.getTypedRuleContext(easmParser.GetMemContext,0)


        def ptr(self):
            return self.getTypedRuleContext(easmParser.PtrContext,0)


        def not_(self):
            return self.getTypedRuleContext(easmParser.NotContext,0)


        def binaryOperator(self):
            return self.getTypedRuleContext(easmParser.BinaryOperatorContext,0)


        def cvalue(self):
            return self.getTypedRuleContext(easmParser.CvalueContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_rvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRvalue" ):
                listener.enterRvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRvalue" ):
                listener.exitRvalue(self)




    def rvalue(self):

        localctx = easmParser.RvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_rvalue)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.newStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.stacksize()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.invoke()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.getMem()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.ptr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 159
                self.not_()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 160
                self.binaryOperator()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 161
                self.cvalue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def getRuleIndex(self):
            return easmParser.RULE_newStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewStat" ):
                listener.enterNewStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewStat" ):
                listener.exitNewStat(self)




    def newStat(self):

        localctx = easmParser.NewStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_newStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(easmParser.T__21)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 165
                self.match(easmParser.T__22)


            self.state = 168
            self.match(easmParser.Id)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PtrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(easmParser.LvalueContext,0)


        def SConst(self):
            return self.getToken(easmParser.SConst, 0)

        def getRuleIndex(self):
            return easmParser.RULE_ptr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPtr" ):
                listener.enterPtr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPtr" ):
                listener.exitPtr(self)




    def ptr(self):

        localctx = easmParser.PtrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ptr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(easmParser.T__23)
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 171
                self.lvalue()
                pass
            elif token in [57]:
                self.state = 172
                self.match(easmParser.SConst)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(easmParser.LvalueContext,0)


        def IConst(self):
            return self.getToken(easmParser.IConst, 0)

        def FConst(self):
            return self.getToken(easmParser.FConst, 0)

        def CConst(self):
            return self.getToken(easmParser.CConst, 0)

        def getRuleIndex(self):
            return easmParser.RULE_not

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)




    def not_(self):

        localctx = easmParser.NotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_not)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(easmParser.T__24)
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 176
                self.lvalue()
                pass
            elif token in [54]:
                self.state = 177
                self.match(easmParser.IConst)
                pass
            elif token in [55]:
                self.state = 178
                self.match(easmParser.FConst)
                pass
            elif token in [56]:
                self.state = 179
                self.match(easmParser.CConst)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StacksizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return easmParser.RULE_stacksize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStacksize" ):
                listener.enterStacksize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStacksize" ):
                listener.exitStacksize(self)




    def stacksize(self):

        localctx = easmParser.StacksizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stacksize)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvokeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def cvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.CvalueContext)
            else:
                return self.getTypedRuleContext(easmParser.CvalueContext,i)


        def getRuleIndex(self):
            return easmParser.RULE_invoke

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvoke" ):
                listener.enterInvoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvoke" ):
                listener.exitInvoke(self)




    def invoke(self):

        localctx = easmParser.InvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_invoke)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(easmParser.T__27)
            self.state = 185
            self.match(easmParser.Id)
            self.state = 186
            self.match(easmParser.T__28)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 279223176896970752) != 0):
                self.state = 187
                self.cvalue()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 188
                    self.match(easmParser.T__29)
                    self.state = 189
                    self.cvalue()
                    self.state = 194
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 197
            self.match(easmParser.T__30)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetMemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.LvalueContext)
            else:
                return self.getTypedRuleContext(easmParser.LvalueContext,i)


        def IConst(self, i:int=None):
            if i is None:
                return self.getTokens(easmParser.IConst)
            else:
                return self.getToken(easmParser.IConst, i)

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def valueType(self):
            return self.getTypedRuleContext(easmParser.ValueTypeContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_getMem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetMem" ):
                listener.enterGetMem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetMem" ):
                listener.exitGetMem(self)




    def getMem(self):

        localctx = easmParser.GetMemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_getMem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 199
                self.match(easmParser.Id)

            elif la_ == 2:
                self.state = 200
                self.valueType()


            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 203
                self.lvalue()
                pass
            elif token in [54]:
                self.state = 204
                self.match(easmParser.IConst)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 207
            self.match(easmParser.T__31)
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 208
                self.lvalue()
                pass
            elif token in [54]:
                self.state = 209
                self.match(easmParser.IConst)
                pass
            elif token in [33]:
                pass
            else:
                pass
            self.state = 212
            self.match(easmParser.T__32)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueType(self):
            return self.getTypedRuleContext(easmParser.ValueTypeContext,0)


        def cvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.CvalueContext)
            else:
                return self.getTypedRuleContext(easmParser.CvalueContext,i)


        def getRuleIndex(self):
            return easmParser.RULE_binaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOperator" ):
                listener.enterBinaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOperator" ):
                listener.exitBinaryOperator(self)




    def binaryOperator(self):

        localctx = easmParser.BinaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_binaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140720308486144) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 215
            self.valueType()
            self.state = 216
            self.cvalue()
            self.state = 217
            self.match(easmParser.T__29)
            self.state = 218
            self.cvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(easmParser.LvalueContext,0)


        def IConst(self):
            return self.getToken(easmParser.IConst, 0)

        def FConst(self):
            return self.getToken(easmParser.FConst, 0)

        def CConst(self):
            return self.getToken(easmParser.CConst, 0)

        def SConst(self):
            return self.getToken(easmParser.SConst, 0)

        def getRuleIndex(self):
            return easmParser.RULE_cvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCvalue" ):
                listener.enterCvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCvalue" ):
                listener.exitCvalue(self)




    def cvalue(self):

        localctx = easmParser.CvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_cvalue)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.lvalue()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(easmParser.IConst)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.match(easmParser.FConst)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.match(easmParser.CConst)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 5)
                self.state = 224
                self.match(easmParser.SConst)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(easmParser.Id, 0)

        def dot(self):
            return self.getTypedRuleContext(easmParser.DotContext,0)


        def cast(self):
            return self.getTypedRuleContext(easmParser.CastContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)




    def lvalue(self):

        localctx = easmParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lvalue)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(easmParser.Id)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.dot()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
                self.cast()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(easmParser.Id)
            else:
                return self.getToken(easmParser.Id, i)

        def valueType(self):
            return self.getTypedRuleContext(easmParser.ValueTypeContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_cast

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCast" ):
                listener.enterCast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCast" ):
                listener.exitCast(self)




    def cast(self):

        localctx = easmParser.CastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_cast)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(easmParser.Id)
            self.state = 233
            self.match(easmParser.T__46)
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 234
                self.match(easmParser.Id)
                pass
            elif token in [49, 50, 51]:
                self.state = 235
                self.valueType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(easmParser.Id)
            else:
                return self.getToken(easmParser.Id, i)

        def getRuleIndex(self):
            return easmParser.RULE_dot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDot" ):
                listener.enterDot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDot" ):
                listener.exitDot(self)




    def dot(self):

        localctx = easmParser.DotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_dot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(easmParser.Id)
            self.state = 239
            self.match(easmParser.Id)
            self.state = 240
            self.match(easmParser.T__47)
            self.state = 241
            self.match(easmParser.Id)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(easmParser.Id)
            else:
                return self.getToken(easmParser.Id, i)

        def valueType(self):
            return self.getTypedRuleContext(easmParser.ValueTypeContext,0)


        def getRuleIndex(self):
            return easmParser.RULE_dataTypeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataTypeDeclaration" ):
                listener.enterDataTypeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataTypeDeclaration" ):
                listener.exitDataTypeDeclaration(self)




    def dataTypeDeclaration(self):

        localctx = easmParser.DataTypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_dataTypeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 243
                self.match(easmParser.Id)
                pass
            elif token in [49, 50, 51]:
                self.state = 244
                self.valueType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 247
            self.match(easmParser.Id)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return easmParser.RULE_valueType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueType" ):
                listener.enterValueType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueType" ):
                listener.exitValueType(self)




    def valueType(self):

        localctx = easmParser.ValueTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_valueType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3940649673949184) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





