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
	| move
	| call
	| push
	| pull	
	| inc
	| dec;

pass: 'pass' SConst;
delete: 'delete' Id;
jump: 'jump' ('if' condition)? 'to' Id;
label: Id ':';
move: rvalue '->' lvalue;
push: 'push' cvalue;
pull: 'pull' lvalue?;
condition: cvalue ( '=' | '!=' | '>' | '<' | '>=' | '<=') cvalue;
inc: 'inc' (lvalue | IConst | FConst | CConst);
dec: 'dec' (lvalue | IConst | FConst | CConst);

rvalue:
	newStat
	| stacksize
	| call
	| getMem
	| array
	| ptr
	| not
	| binaryOperator
	| cvalue;

newStat: 'new' 'local'? Id;
call: 'call' Id ('(' ( cvalue (',' cvalue)*)? ')')?;
array: 'array' IConst;
ptr: 'ptr' (lvalue | SConst);
not: 'not' (lvalue | IConst | FConst | CConst);
stacksize: 'ssize';

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

lvalue: Id | dot | cast | getMem;
cast: Id 'as' (Id | valueType);
dot: Id Id '.' Id;
getMem: (Id | valueType)? (Id | dot | cast | IConst) '[' (Id | dot | cast | IConst)? ']';

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