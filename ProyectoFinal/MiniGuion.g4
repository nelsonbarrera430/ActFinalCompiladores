grammar MiniGuion;

program    : scene+ EOF ;
scene      : 'escena' ID '{' dialogue+ '}' ;
dialogue   : decir_stmt | opcion_stmt ;
decir_stmt : 'decir' STRING ';' ;
opcion_stmt: 'opcion' STRING 'ir_a' ID ';' ;

ID         : [a-zA-Z_] [a-zA-Z_0-9]* ;
STRING     : '"' ( ~["\\] | '\\' . )* '"' ;
WS         : [ \t\r\n]+ -> skip ;
COMMENT    : '//' ~[\r\n]* -> skip ;
