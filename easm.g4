grammar easm;

program: Pony (importStat | function | structure | pass)* EOF;

structure: 'struct' Id dataTypeDeclaration+;

function:
	'func' Id ('(' (Id (',' Id)*)? ')')? (
		'[' (Id (',' Id)*)? ']'
	)? expression*;
importStat: 'import' 'native'? SConst;

expression:
	pass
	| delete
	| jump
	| label
	| move
	| call
	| push
	| pull
	| inc
	| dec
	| ret;

pass: 'pass' SConst;
delete: 'delete' Id;
jump: 'jump' ('if' (condition | cvalue))? 'to' Id;
label: Id ':';
move: rvalue '->' lvalue;
push: 'push' cvalue;
pull: 'pull' lvalue?;
inc: 'inc' (lvalue | IConst | FConst | CConst);
dec: 'dec' (lvalue | IConst | FConst | CConst);
ret: 'return' cvalue (',' cvalue)*;

rvalue:
	newStat
	| stacksize
	| call
	| getMem
	| heap
	| array
	| ptr
	| not
	| bool
	| condition
	| binaryOperator
	| cvalue;

newStat: 'new' 'local'? Id;
call:
	'call' 'native'? Id ('(' ( cvalue (',' cvalue)*)? ')')? (
		'[' (lvalue (',' lvalue)*)? ']'
	)?;
heap: 'heap' (Id | valueType | SConst)? '[' IConst ']';
array: 'array' (Id | valueType | SConst)? '[' IConst ']';
ptr: 'ptr' (lvalue | SConst);
not: 'not' (lvalue | IConst | FConst | CConst);
bool: 'bool' (lvalue | IConst | FConst | CConst);
condition: cvalue ( '=' | '!=' | '>' | '<' | '>=' | '<=') cvalue;
stacksize: 'ssize';

binaryOperator: ('add' | 'sub' | 'mul' | 'div') valueType? cvalue ',' cvalue
	| (
		'and'
		| 'or'
		| 'xor'
		| 'nor'
		| 'nand'
		| 'xnor'
		| 'rem'
		| 'shr'
		| 'shl'
	) cvalue ',' cvalue;

cvalue: lvalue | IConst | FConst | CConst | SConst;

lvalue: Id | dot | cast | getMem;
cast: (Id | getMem | dot) 'as' (Id | valueType | SConst);
dot: Id Id '.' Id;
getMem: (Id | valueType)? (Id | dot | IConst) '[' (
		Id
		| dot
		| IConst
	)? ']';

dataTypeDeclaration: (Id | valueType) Id;

valueType: 'int' | 'float' | 'string' | 'byte';

Pony: [pP][oO][nN][yY][!.,:]?;

IConst:
	'null'
	| 'true'
	| 'false'
	| [+-]? (
		Digits
		| '0' [oO] [0-7]+
		| '0' [xX] [0-9a-fA-F]+
		| '0' [bB] [0-1]+
	)
	;
	
Id: '*'? [a-zA-Z_][a-zA-Z_0-9]*;

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