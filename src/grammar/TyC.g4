grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit()
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text)
    else:
        return super().emit()
}



options{
	language=Python3;
}

// TODO: Define grammar rules here
/* =========================
 *  PARSER RULES (BNF form)
 * ========================= */

program
    : declList EOF
    ;

declList
    : decl declList
    |   // epsilon
    ;

decl
    : structDecl
    | funcDecl
    ;

structDecl
    : STRUCT ID LBRACE structMemberList RBRACE SEMI
    ;

structMemberList
    : structMember structMemberList
    |   // epsilon
    ;

structMember
    : type idList SEMI
    ;

funcDecl
    : funcHead LPAREN paramListOpt RPAREN block
    ;

funcHead
    : typeOrVoid ID
    | ID
    ;

typeOrVoid
    : type
    | VOID
    ;

paramListOpt
    : paramList
    |   // epsilon
    ;

paramList
    : param paramListTail
    ;

paramListTail
    : COMMA param paramListTail
    |   // epsilon
    ;

param
    : paramType ID
    ;

paramType
    : INT
    | FLOAT
    | STRING
    | ID
    ;

type
    : INT
    | FLOAT
    | STRING
    | AUTO
    | ID
    ;

idList
    : ID idListTail
    ;

idListTail
    : COMMA ID idListTail
    |   // epsilon
    ;

block
    : LBRACE blockItemList RBRACE
    ;

blockItemList
    : blockItem blockItemList
    |   // epsilon
    ;

blockItem
    : varDeclStmt
    | stmt
    ;

varDeclStmt
    : type varDeclList SEMI
    ;

varDeclList
    : varDecl varDeclListTail
    ;

varDeclListTail
    : COMMA varDecl varDeclListTail
    |   // epsilon
    ;

varDecl
    : ID varInitOpt
    ;

varInitOpt
    : ASSIGN expr
    |   // epsilon
    ;

/* ----- statements ----- */

stmt
    : block
    | ifStmt
    | whileStmt
    | forStmt
    | switchStmt
    | breakStmt
    | continueStmt
    | returnStmt
    | exprStmt
    | SEMI
    ;

ifStmt
    : IF LPAREN expr RPAREN stmt elseOpt
    ;

elseOpt
    : ELSE stmt
    |   // epsilon
    ;

whileStmt
    : WHILE LPAREN expr RPAREN stmt
    ;

forStmt
    : FOR LPAREN forInitOpt SEMI exprOpt SEMI forUpdateOpt RPAREN stmt
    ;

forInitOpt
    : forInit
    |   // epsilon
    ;

forInit
    : varDeclFor
    | exprList
    ;

varDeclFor
    : type varDeclList
    ;

exprOpt
    : expr
    |   // epsilon
    ;

forUpdateOpt
    : forUpdate
    |   // epsilon
    ;

forUpdate
    : exprList
    ;

switchStmt
    : SWITCH LPAREN expr RPAREN LBRACE switchClauseList RBRACE
    ;

switchClauseList
    : switchClause switchClauseList
    |   // epsilon
    ;

switchClause
    : CASE expr COLON blockItemList
    | DEFAULT COLON blockItemList
    ;

breakStmt
    : BREAK SEMI
    ;

continueStmt
    : CONTINUE SEMI
    ;

returnStmt
    : RETURN exprOpt SEMI
    ;

exprStmt
    : expr SEMI
    ;

exprList
    : expr exprListTail
    ;

exprListTail
    : COMMA expr exprListTail
    |   // epsilon
    ;

/* ----- expressions (precedence) ----- */

expr
    : assignExpr
    ;

assignExpr
    : orExpr assignOpt
    ;

assignOpt
    : ASSIGN assignExpr
    |   // epsilon
    ;

orExpr
    : andExpr orTail
    ;

orTail
    : OR andExpr orTail
    |   // epsilon
    ;

andExpr
    : eqExpr andTail
    ;

andTail
    : AND eqExpr andTail
    |   // epsilon
    ;

eqExpr
    : relExpr eqTail
    ;

eqTail
    : eqOp relExpr eqTail
    |   // epsilon
    ;

eqOp
    : EQ
    | NEQ
    ;

relExpr
    : addExpr relTail
    ;

relTail
    : relOp addExpr relTail
    |   // epsilon
    ;

relOp
    : LT
    | LTE
    | GT
    | GTE
    ;

addExpr
    : mulExpr addTail
    ;

addTail
    : addOp mulExpr addTail
    |   // epsilon
    ;

addOp
    : PLUS
    | MINUS
    ;

mulExpr
    : unaryExpr mulTail
    ;

mulTail
    : mulOp unaryExpr mulTail
    |   // epsilon
    ;

mulOp
    : MUL
    | DIV
    | MOD
    ;

unaryExpr
    : unaryPrefix unaryExpr
    | postfixExpr
    ;

unaryPrefix
    : NOT
    | PLUS
    | MINUS
    | INC
    | DEC
    ;

postfixExpr
    : primaryExpr postfixSuffixList
    ;

postfixSuffixList
    : postfixSuffix postfixSuffixList
    |   // epsilon
    ;

postfixSuffix
    : INC
    | DEC
    | DOT ID
    | LPAREN argListOpt RPAREN
    ;

argListOpt
    : argList
    |   // epsilon
    ;

argList
    : expr argListTail
    ;

argListTail
    : COMMA expr argListTail
    |   // epsilon
    ;

primaryExpr
    : literal
    | ID
    | LPAREN expr RPAREN
    | structLiteral
    ;

literal
    : INT_LIT
    | FLOAT_LIT
    | STRING_LIT
    ;

structLiteral
    : LBRACE structElemsOpt RBRACE
    ;

structElemsOpt
    : structElems
    |   // epsilon
    ;

structElems
    : expr structElemsTail
    ;

structElemsTail
    : COMMA expr structElemsTail
    |   // epsilon
    ;

/* =========================
 *  LEXER RULES
 * ========================= */

/* ----- keywords ----- */
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

/* ----- operators ----- */
EQ: '==';
NEQ: '!=';
LTE: '<=';
GTE: '>=';
OR: '||';
AND: '&&';
INC: '++';
DEC: '--';

ASSIGN: '=';
LT: '<';
GT: '>';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
DOT: '.';

/* ----- separators ----- */
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
COMMA: ',';
COLON: ':';

/* ----- identifiers ----- */
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

/* ----- numbers ----- */
INT_LIT
    : DIGIT+
    ;

FLOAT_LIT
    : DIGIT+ '.' DIGIT* EXP?
    | '.' DIGIT+ EXP?
    | DIGIT+ EXP
    ;

fragment EXP
    : [eE] [+-]? DIGIT+
    ;

fragment DIGIT
    : [0-9]
    ;

/* ----- strings & errors ----- */
STRING_LIT
    : '"' STR_CHAR* '"'
      { self.text = self.text[1:-1] }     // strip quotes for normal strings
    ;

fragment STR_CHAR
    : ESC_SEQ
    | ~["\\\r\n]
    ;

fragment ESC_SEQ
    : '\\' [bfrnt"\\]
    ;

// ILLEGAL_ESCAPE must come BEFORE UNCLOSE_STRING so it wins on `"ab\q` (EOF)
ILLEGAL_ESCAPE
    : '"' (ESC_SEQ | ~["\\\r\n])* '\\' ~[bfrnt"\\]
      { self.text = self.text[1:] }       // remove opening quote
    ;

UNCLOSE_STRING
    : '"' (ESC_SEQ | ~["\\\r\n])*
      ( '\r' '\n'? | '\n' | EOF )
      {
        # remove opening quote and also trim trailing newline chars if present
        if self.text.endswith('\r\n'):
            self.text = self.text[1:-2]
        elif self.text.endswith('\n') or self.text.endswith('\r'):
            self.text = self.text[1:-1]
        else:
            self.text = self.text[1:]
      }
    ;

/* ----- comments & whitespace ----- */
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

/* ----- fallback error ----- */
ERROR_CHAR
    : .
    ;