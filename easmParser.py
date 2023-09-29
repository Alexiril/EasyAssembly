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
        4,1,62,301,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,1,0,1,0,5,0,
        68,8,0,10,0,12,0,71,9,0,1,0,1,0,1,1,1,1,1,1,4,1,78,8,1,11,1,12,1,
        79,1,2,1,2,1,2,1,2,5,2,86,8,2,10,2,12,2,89,9,2,3,2,91,8,2,1,2,3,
        2,94,8,2,1,2,1,2,1,2,5,2,99,8,2,10,2,12,2,102,9,2,1,3,1,3,3,3,106,
        8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,121,
        8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,3,7,132,8,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,3,11,149,8,
        11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,160,8,13,1,
        14,1,14,1,14,1,14,1,14,3,14,167,8,14,1,15,1,15,1,15,1,15,5,15,173,
        8,15,10,15,12,15,176,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,187,8,16,1,17,1,17,3,17,191,8,17,1,17,1,17,1,18,1,18,3,
        18,197,8,18,1,18,1,18,1,18,1,18,1,18,5,18,204,8,18,10,18,12,18,207,
        9,18,3,18,209,8,18,1,18,3,18,212,8,18,1,18,1,18,1,18,1,18,5,18,218,
        8,18,10,18,12,18,221,9,18,1,18,1,18,3,18,225,8,18,1,19,1,19,1,19,
        1,20,1,20,1,20,3,20,233,8,20,1,21,1,21,1,21,1,21,1,21,3,21,240,8,
        21,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,
        24,3,24,255,8,24,1,25,1,25,1,25,1,25,3,25,261,8,25,1,26,1,26,1,26,
        1,26,3,26,267,8,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,3,28,276,8,
        28,1,28,1,28,1,28,1,28,3,28,282,8,28,1,28,1,28,1,28,1,28,1,28,3,
        28,289,8,28,1,28,1,28,1,29,1,29,3,29,295,8,29,1,29,1,29,1,30,1,30,
        1,30,0,0,31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,0,3,1,0,17,22,1,0,35,47,1,0,
        50,52,335,0,62,1,0,0,0,2,74,1,0,0,0,4,93,1,0,0,0,6,103,1,0,0,0,8,
        120,1,0,0,0,10,122,1,0,0,0,12,125,1,0,0,0,14,128,1,0,0,0,16,136,
        1,0,0,0,18,139,1,0,0,0,20,143,1,0,0,0,22,146,1,0,0,0,24,150,1,0,
        0,0,26,154,1,0,0,0,28,161,1,0,0,0,30,168,1,0,0,0,32,186,1,0,0,0,
        34,188,1,0,0,0,36,194,1,0,0,0,38,226,1,0,0,0,40,229,1,0,0,0,42,234,
        1,0,0,0,44,241,1,0,0,0,46,243,1,0,0,0,48,254,1,0,0,0,50,260,1,0,
        0,0,52,262,1,0,0,0,54,268,1,0,0,0,56,275,1,0,0,0,58,294,1,0,0,0,
        60,298,1,0,0,0,62,69,5,53,0,0,63,68,3,6,3,0,64,68,3,4,2,0,65,68,
        3,2,1,0,66,68,3,10,5,0,67,63,1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,
        67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,
        0,0,0,71,69,1,0,0,0,72,73,5,0,0,1,73,1,1,0,0,0,74,75,5,1,0,0,75,
        77,5,54,0,0,76,78,3,58,29,0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,
        0,0,0,79,80,1,0,0,0,80,3,1,0,0,0,81,90,5,2,0,0,82,87,5,54,0,0,83,
        84,5,3,0,0,84,86,5,54,0,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,
        0,0,87,88,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,90,82,1,0,0,0,90,91,
        1,0,0,0,91,92,1,0,0,0,92,94,5,4,0,0,93,81,1,0,0,0,93,94,1,0,0,0,
        94,95,1,0,0,0,95,96,5,5,0,0,96,100,5,54,0,0,97,99,3,8,4,0,98,97,
        1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,5,1,0,
        0,0,102,100,1,0,0,0,103,105,5,6,0,0,104,106,5,7,0,0,105,104,1,0,
        0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,58,0,0,108,7,1,0,0,
        0,109,121,3,10,5,0,110,121,3,12,6,0,111,121,3,14,7,0,112,121,3,16,
        8,0,113,121,3,18,9,0,114,121,3,36,18,0,115,121,3,20,10,0,116,121,
        3,22,11,0,117,121,3,26,13,0,118,121,3,28,14,0,119,121,3,30,15,0,
        120,109,1,0,0,0,120,110,1,0,0,0,120,111,1,0,0,0,120,112,1,0,0,0,
        120,113,1,0,0,0,120,114,1,0,0,0,120,115,1,0,0,0,120,116,1,0,0,0,
        120,117,1,0,0,0,120,118,1,0,0,0,120,119,1,0,0,0,121,9,1,0,0,0,122,
        123,5,8,0,0,123,124,5,58,0,0,124,11,1,0,0,0,125,126,5,9,0,0,126,
        127,5,54,0,0,127,13,1,0,0,0,128,131,5,10,0,0,129,130,5,11,0,0,130,
        132,3,24,12,0,131,129,1,0,0,0,131,132,1,0,0,0,132,133,1,0,0,0,133,
        134,5,12,0,0,134,135,5,54,0,0,135,15,1,0,0,0,136,137,5,54,0,0,137,
        138,5,13,0,0,138,17,1,0,0,0,139,140,3,32,16,0,140,141,5,14,0,0,141,
        142,3,50,25,0,142,19,1,0,0,0,143,144,5,15,0,0,144,145,3,48,24,0,
        145,21,1,0,0,0,146,148,5,16,0,0,147,149,3,50,25,0,148,147,1,0,0,
        0,148,149,1,0,0,0,149,23,1,0,0,0,150,151,3,48,24,0,151,152,7,0,0,
        0,152,153,3,48,24,0,153,25,1,0,0,0,154,159,5,23,0,0,155,160,3,50,
        25,0,156,160,5,55,0,0,157,160,5,56,0,0,158,160,5,57,0,0,159,155,
        1,0,0,0,159,156,1,0,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,27,1,
        0,0,0,161,166,5,24,0,0,162,167,3,50,25,0,163,167,5,55,0,0,164,167,
        5,56,0,0,165,167,5,57,0,0,166,162,1,0,0,0,166,163,1,0,0,0,166,164,
        1,0,0,0,166,165,1,0,0,0,167,29,1,0,0,0,168,169,5,25,0,0,169,174,
        3,48,24,0,170,171,5,3,0,0,171,173,3,48,24,0,172,170,1,0,0,0,173,
        176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,31,1,0,0,0,176,174,
        1,0,0,0,177,187,3,34,17,0,178,187,3,44,22,0,179,187,3,36,18,0,180,
        187,3,56,28,0,181,187,3,38,19,0,182,187,3,40,20,0,183,187,3,42,21,
        0,184,187,3,46,23,0,185,187,3,48,24,0,186,177,1,0,0,0,186,178,1,
        0,0,0,186,179,1,0,0,0,186,180,1,0,0,0,186,181,1,0,0,0,186,182,1,
        0,0,0,186,183,1,0,0,0,186,184,1,0,0,0,186,185,1,0,0,0,187,33,1,0,
        0,0,188,190,5,26,0,0,189,191,5,27,0,0,190,189,1,0,0,0,190,191,1,
        0,0,0,191,192,1,0,0,0,192,193,5,54,0,0,193,35,1,0,0,0,194,196,5,
        28,0,0,195,197,5,7,0,0,196,195,1,0,0,0,196,197,1,0,0,0,197,198,1,
        0,0,0,198,211,5,54,0,0,199,208,5,29,0,0,200,205,3,48,24,0,201,202,
        5,3,0,0,202,204,3,48,24,0,203,201,1,0,0,0,204,207,1,0,0,0,205,203,
        1,0,0,0,205,206,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,208,200,
        1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,212,5,30,0,0,211,199,
        1,0,0,0,211,212,1,0,0,0,212,224,1,0,0,0,213,214,5,2,0,0,214,219,
        3,50,25,0,215,216,5,3,0,0,216,218,3,50,25,0,217,215,1,0,0,0,218,
        221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,222,1,0,0,0,221,
        219,1,0,0,0,222,223,5,4,0,0,223,225,1,0,0,0,224,213,1,0,0,0,224,
        225,1,0,0,0,225,37,1,0,0,0,226,227,5,31,0,0,227,228,5,55,0,0,228,
        39,1,0,0,0,229,232,5,32,0,0,230,233,3,50,25,0,231,233,5,58,0,0,232,
        230,1,0,0,0,232,231,1,0,0,0,233,41,1,0,0,0,234,239,5,33,0,0,235,
        240,3,50,25,0,236,240,5,55,0,0,237,240,5,56,0,0,238,240,5,57,0,0,
        239,235,1,0,0,0,239,236,1,0,0,0,239,237,1,0,0,0,239,238,1,0,0,0,
        240,43,1,0,0,0,241,242,5,34,0,0,242,45,1,0,0,0,243,244,7,1,0,0,244,
        245,3,60,30,0,245,246,3,48,24,0,246,247,5,3,0,0,247,248,3,48,24,
        0,248,47,1,0,0,0,249,255,3,50,25,0,250,255,5,55,0,0,251,255,5,56,
        0,0,252,255,5,57,0,0,253,255,5,58,0,0,254,249,1,0,0,0,254,250,1,
        0,0,0,254,251,1,0,0,0,254,252,1,0,0,0,254,253,1,0,0,0,255,49,1,0,
        0,0,256,261,5,54,0,0,257,261,3,54,27,0,258,261,3,52,26,0,259,261,
        3,56,28,0,260,256,1,0,0,0,260,257,1,0,0,0,260,258,1,0,0,0,260,259,
        1,0,0,0,261,51,1,0,0,0,262,263,5,54,0,0,263,266,5,48,0,0,264,267,
        5,54,0,0,265,267,3,60,30,0,266,264,1,0,0,0,266,265,1,0,0,0,267,53,
        1,0,0,0,268,269,5,54,0,0,269,270,5,54,0,0,270,271,5,49,0,0,271,272,
        5,54,0,0,272,55,1,0,0,0,273,276,5,54,0,0,274,276,3,60,30,0,275,273,
        1,0,0,0,275,274,1,0,0,0,275,276,1,0,0,0,276,281,1,0,0,0,277,282,
        5,54,0,0,278,282,3,54,27,0,279,282,3,52,26,0,280,282,5,55,0,0,281,
        277,1,0,0,0,281,278,1,0,0,0,281,279,1,0,0,0,281,280,1,0,0,0,282,
        283,1,0,0,0,283,288,5,2,0,0,284,289,5,54,0,0,285,289,3,54,27,0,286,
        289,3,52,26,0,287,289,5,55,0,0,288,284,1,0,0,0,288,285,1,0,0,0,288,
        286,1,0,0,0,288,287,1,0,0,0,288,289,1,0,0,0,289,290,1,0,0,0,290,
        291,5,4,0,0,291,57,1,0,0,0,292,295,5,54,0,0,293,295,3,60,30,0,294,
        292,1,0,0,0,294,293,1,0,0,0,295,296,1,0,0,0,296,297,5,54,0,0,297,
        59,1,0,0,0,298,299,7,2,0,0,299,61,1,0,0,0,31,67,69,79,87,90,93,100,
        105,120,131,148,159,166,174,186,190,196,205,208,211,219,224,232,
        239,254,260,266,275,281,288,294
    ]

class easmParser ( Parser ):

    grammarFileName = "easm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'['", "','", "']'", "'func'", 
                     "'import'", "'native'", "'pass'", "'delete'", "'jump'", 
                     "'if'", "'to'", "':'", "'->'", "'push'", "'pull'", 
                     "'='", "'!='", "'>'", "'<'", "'>='", "'<='", "'inc'", 
                     "'dec'", "'return'", "'new'", "'local'", "'call'", 
                     "'('", "')'", "'array'", "'ptr'", "'not'", "'ssize'", 
                     "'and'", "'or'", "'xor'", "'nor'", "'nand'", "'xnor'", 
                     "'add'", "'sub'", "'mul'", "'div'", "'rem'", "'shr'", 
                     "'shl'", "'as'", "'.'", "'int'", "'float'", "'string'" ]

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
                      "<INVALID>", "Pony", "Id", "IConst", "FConst", "CConst", 
                      "SConst", "Whitespace", "Newline", "BlockComment", 
                      "LineComment" ]

    RULE_program = 0
    RULE_structure = 1
    RULE_function = 2
    RULE_importStat = 3
    RULE_expression = 4
    RULE_pass = 5
    RULE_delete = 6
    RULE_jump = 7
    RULE_label = 8
    RULE_move = 9
    RULE_push = 10
    RULE_pull = 11
    RULE_condition = 12
    RULE_inc = 13
    RULE_dec = 14
    RULE_ret = 15
    RULE_rvalue = 16
    RULE_newStat = 17
    RULE_call = 18
    RULE_array = 19
    RULE_ptr = 20
    RULE_not = 21
    RULE_stacksize = 22
    RULE_binaryOperator = 23
    RULE_cvalue = 24
    RULE_lvalue = 25
    RULE_cast = 26
    RULE_dot = 27
    RULE_getMem = 28
    RULE_dataTypeDeclaration = 29
    RULE_valueType = 30

    ruleNames =  [ "program", "structure", "function", "importStat", "expression", 
                   "pass", "delete", "jump", "label", "move", "push", "pull", 
                   "condition", "inc", "dec", "ret", "rvalue", "newStat", 
                   "call", "array", "ptr", "not", "stacksize", "binaryOperator", 
                   "cvalue", "lvalue", "cast", "dot", "getMem", "dataTypeDeclaration", 
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
    T__51=52
    Pony=53
    Id=54
    IConst=55
    FConst=56
    CConst=57
    SConst=58
    Whitespace=59
    Newline=60
    BlockComment=61
    LineComment=62

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
            self.state = 62
            self.match(easmParser.Pony)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 358) != 0):
                self.state = 67
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 63
                    self.importStat()
                    pass
                elif token in [2, 5]:
                    self.state = 64
                    self.function()
                    pass
                elif token in [1]:
                    self.state = 65
                    self.structure()
                    pass
                elif token in [8]:
                    self.state = 66
                    self.pass_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
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
            self.state = 74
            self.match(easmParser.T__0)
            self.state = 75
            self.match(easmParser.Id)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.dataTypeDeclaration()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25895697857380352) != 0)):
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

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(easmParser.Id)
            else:
                return self.getToken(easmParser.Id, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 81
                self.match(easmParser.T__1)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==54:
                    self.state = 82
                    self.match(easmParser.Id)
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==3:
                        self.state = 83
                        self.match(easmParser.T__2)
                        self.state = 84
                        self.match(easmParser.Id)
                        self.state = 89
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 92
                self.match(easmParser.T__3)


            self.state = 95
            self.match(easmParser.T__4)
            self.state = 96
            self.match(easmParser.Id)
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 97
                    self.expression() 
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 103
            self.match(easmParser.T__5)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 104
                self.match(easmParser.T__6)


            self.state = 107
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


        def move(self):
            return self.getTypedRuleContext(easmParser.MoveContext,0)


        def call(self):
            return self.getTypedRuleContext(easmParser.CallContext,0)


        def push(self):
            return self.getTypedRuleContext(easmParser.PushContext,0)


        def pull(self):
            return self.getTypedRuleContext(easmParser.PullContext,0)


        def inc(self):
            return self.getTypedRuleContext(easmParser.IncContext,0)


        def dec(self):
            return self.getTypedRuleContext(easmParser.DecContext,0)


        def ret(self):
            return self.getTypedRuleContext(easmParser.RetContext,0)


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
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.pass_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.delete()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.jump()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.label()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.move()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 114
                self.call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 115
                self.push()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 116
                self.pull()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 117
                self.inc()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 118
                self.dec()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 119
                self.ret()
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
            self.state = 122
            self.match(easmParser.T__7)
            self.state = 123
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
            self.state = 125
            self.match(easmParser.T__8)
            self.state = 126
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
            self.state = 128
            self.match(easmParser.T__9)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 129
                self.match(easmParser.T__10)
                self.state = 130
                self.condition()


            self.state = 133
            self.match(easmParser.T__11)
            self.state = 134
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
            self.state = 136
            self.match(easmParser.Id)
            self.state = 137
            self.match(easmParser.T__12)
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
        self.enterRule(localctx, 18, self.RULE_move)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.rvalue()
            self.state = 140
            self.match(easmParser.T__13)
            self.state = 141
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
        self.enterRule(localctx, 20, self.RULE_push)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(easmParser.T__14)
            self.state = 144
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
        self.enterRule(localctx, 22, self.RULE_pull)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(easmParser.T__15)
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 147
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
        self.enterRule(localctx, 24, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.cvalue()
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 152
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
        self.enterRule(localctx, 26, self.RULE_inc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(easmParser.T__22)
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 155
                self.lvalue()
                pass

            elif la_ == 2:
                self.state = 156
                self.match(easmParser.IConst)
                pass

            elif la_ == 3:
                self.state = 157
                self.match(easmParser.FConst)
                pass

            elif la_ == 4:
                self.state = 158
                self.match(easmParser.CConst)
                pass


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
        self.enterRule(localctx, 28, self.RULE_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(easmParser.T__23)
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 162
                self.lvalue()
                pass

            elif la_ == 2:
                self.state = 163
                self.match(easmParser.IConst)
                pass

            elif la_ == 3:
                self.state = 164
                self.match(easmParser.FConst)
                pass

            elif la_ == 4:
                self.state = 165
                self.match(easmParser.CConst)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
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
            return easmParser.RULE_ret

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)




    def ret(self):

        localctx = easmParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ret)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(easmParser.T__24)
            self.state = 169
            self.cvalue()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 170
                self.match(easmParser.T__2)
                self.state = 171
                self.cvalue()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def call(self):
            return self.getTypedRuleContext(easmParser.CallContext,0)


        def getMem(self):
            return self.getTypedRuleContext(easmParser.GetMemContext,0)


        def array(self):
            return self.getTypedRuleContext(easmParser.ArrayContext,0)


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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.newStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.stacksize()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.getMem()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 181
                self.array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 182
                self.ptr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 183
                self.not_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 184
                self.binaryOperator()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 185
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
            self.state = 188
            self.match(easmParser.T__25)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 189
                self.match(easmParser.T__26)


            self.state = 192
            self.match(easmParser.Id)
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

        def lvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.LvalueContext)
            else:
                return self.getTypedRuleContext(easmParser.LvalueContext,i)


        def cvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.CvalueContext)
            else:
                return self.getTypedRuleContext(easmParser.CvalueContext,i)


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
        self.enterRule(localctx, 36, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(easmParser.T__27)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 195
                self.match(easmParser.T__6)


            self.state = 198
            self.match(easmParser.Id)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 199
                self.match(easmParser.T__28)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 566327653141839872) != 0):
                    self.state = 200
                    self.cvalue()
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==3:
                        self.state = 201
                        self.match(easmParser.T__2)
                        self.state = 202
                        self.cvalue()
                        self.state = 207
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 210
                self.match(easmParser.T__29)


            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 213
                self.match(easmParser.T__1)
                self.state = 214
                self.lvalue()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 215
                    self.match(easmParser.T__2)
                    self.state = 216
                    self.lvalue()
                    self.state = 221
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 222
                self.match(easmParser.T__3)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IConst(self):
            return self.getToken(easmParser.IConst, 0)

        def getRuleIndex(self):
            return easmParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = easmParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(easmParser.T__30)
            self.state = 227
            self.match(easmParser.IConst)
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
        self.enterRule(localctx, 40, self.RULE_ptr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(easmParser.T__31)
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50, 51, 52, 54, 55]:
                self.state = 230
                self.lvalue()
                pass
            elif token in [58]:
                self.state = 231
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
        self.enterRule(localctx, 42, self.RULE_not)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(easmParser.T__32)
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 235
                self.lvalue()
                pass

            elif la_ == 2:
                self.state = 236
                self.match(easmParser.IConst)
                pass

            elif la_ == 3:
                self.state = 237
                self.match(easmParser.FConst)
                pass

            elif la_ == 4:
                self.state = 238
                self.match(easmParser.CConst)
                pass


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
        self.enterRule(localctx, 44, self.RULE_stacksize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(easmParser.T__33)
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
            self.state = 243
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 281440616972288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 244
            self.valueType()
            self.state = 245
            self.cvalue()
            self.state = 246
            self.match(easmParser.T__2)
            self.state = 247
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
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.lvalue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(easmParser.IConst)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.match(easmParser.FConst)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.match(easmParser.CConst)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 253
                self.match(easmParser.SConst)
                pass


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


        def getMem(self):
            return self.getTypedRuleContext(easmParser.GetMemContext,0)


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
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(easmParser.Id)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.dot()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.cast()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.getMem()
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
            self.state = 262
            self.match(easmParser.Id)
            self.state = 263
            self.match(easmParser.T__47)
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.state = 264
                self.match(easmParser.Id)
                pass
            elif token in [50, 51, 52]:
                self.state = 265
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
            self.state = 268
            self.match(easmParser.Id)
            self.state = 269
            self.match(easmParser.Id)
            self.state = 270
            self.match(easmParser.T__48)
            self.state = 271
            self.match(easmParser.Id)
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

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(easmParser.Id)
            else:
                return self.getToken(easmParser.Id, i)

        def dot(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.DotContext)
            else:
                return self.getTypedRuleContext(easmParser.DotContext,i)


        def cast(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(easmParser.CastContext)
            else:
                return self.getTypedRuleContext(easmParser.CastContext,i)


        def IConst(self, i:int=None):
            if i is None:
                return self.getTokens(easmParser.IConst)
            else:
                return self.getToken(easmParser.IConst, i)

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
        self.enterRule(localctx, 56, self.RULE_getMem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 273
                self.match(easmParser.Id)

            elif la_ == 2:
                self.state = 274
                self.valueType()


            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 277
                self.match(easmParser.Id)
                pass

            elif la_ == 2:
                self.state = 278
                self.dot()
                pass

            elif la_ == 3:
                self.state = 279
                self.cast()
                pass

            elif la_ == 4:
                self.state = 280
                self.match(easmParser.IConst)
                pass


            self.state = 283
            self.match(easmParser.T__1)
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 284
                self.match(easmParser.Id)

            elif la_ == 2:
                self.state = 285
                self.dot()

            elif la_ == 3:
                self.state = 286
                self.cast()

            elif la_ == 4:
                self.state = 287
                self.match(easmParser.IConst)


            self.state = 290
            self.match(easmParser.T__3)
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
        self.enterRule(localctx, 58, self.RULE_dataTypeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.state = 292
                self.match(easmParser.Id)
                pass
            elif token in [50, 51, 52]:
                self.state = 293
                self.valueType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 296
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
        self.enterRule(localctx, 60, self.RULE_valueType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7881299347898368) != 0)):
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





