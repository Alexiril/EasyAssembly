grammar easm;

program: Pony (importStat | function | structure | pass)* EOF;

structure: 'struct' Id dataTypeDeclaration+;

function: 'func' Id expression*;
importStat: 'import' 'native'? SConst;

expression:
	pass
	| delete
	| jump
	| label
	| call
	| move
	| push
	| pull	
	| inc
	| dec
	| invoke;

pass: 'pass' SConst;
delete: 'delete' Id;
jump: 'jump' ('if' condition)? Id;
label: Id ':';
call: 'call' Id;
move: rvalue '->' lvalue;
push: 'push' cvalue;
pull: 'pull' lvalue?;
condition: cvalue ( '=' | '!=' | '>' | '<' | '>=' | '<=') cvalue;
inc: 'inc' (lvalue | IConst | FConst | CConst);
dec: 'dec' (lvalue | IConst | FConst | CConst);

rvalue:
	newStat
	| stacksize
	| invoke
	| getMem
	| ptr
	| not
	| binaryOperator
	| cvalue;

newStat: 'new' 'local'? Id;
ptr: 'ptr' (lvalue | SConst);
not: 'not' (lvalue | IConst | FConst | CConst);
stacksize: 'stack size' | 'ssize';
invoke: 'invoke' Id '(' ( cvalue (',' cvalue)*)? ')';
getMem: (Id | valueType)? (lvalue | IConst) '[' (lvalue | IConst)? ']';
binaryOperator: (
		'and'
		| 'or'
		| 'xor'
		| 'nor'
		| 'nand'
		| 'xnor'
		| 'add'
		| 'sub'
		| 'mul'
		| 'div'
		| 'rem'
		| 'shr'
		| 'shl'
	) valueType cvalue ',' cvalue;

cvalue: lvalue | IConst | FConst | CConst | SConst;

lvalue: Id | dot | cast;
cast: Id 'as' (Id | valueType);
dot: Id Id '.' Id;

dataTypeDeclaration: (Id | valueType) Id;

valueType: 'int' | 'float' | 'string';

Pony: [pP][oO][nN][yY][!.,:]?;
Id: [a-zA-Z_][a-zA-Z_0-9]*;

IConst:
	[+-]? (
		Digits
		| '0' [oO] [0-7]+
		| '0' [xX] [0-9a-fA-F]+
		| '0' [bB] [0-1]+
	);

FConst: [+-]? (Fract Exp? | Digits Exp);
fragment Fract: Digits? '.' Digits | Digits '.';
fragment Exp: [eE] [+-]? Digits;

fragment Digits: [0-9]+;

CConst:
	'\'' CharSeq '\''
	| 'L\'' CharSeq '\''
	| 'u\'' CharSeq '\''
	| 'U\'' CharSeq '\'';
fragment CharSeq: (~['\\\r\n] | EscSeq)+;
fragment EscSeq: '\\' ['"?abfnrtv\\] | '\\x' [0-9a-fA-F]+;

SConst: ('u8' | 'u' | 'U' | 'L')? '"' (ExtChar+)? '"';
fragment ExtChar: ~["\\\r\n] | EscSeq | '\\\n' | '\\\r\n';

Whitespace: [ \t]+ -> channel(HIDDEN);
Newline: ( '\r' '\n'? | '\n') -> channel(HIDDEN);
BlockComment: '/*' .*? '*/' -> channel(HIDDEN);
LineComment: '//' ~[\r\n]* -> channel(HIDDEN);