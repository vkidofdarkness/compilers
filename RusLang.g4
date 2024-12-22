grammar RusLang;

// ----------------------------------------------------------------------------
// 1. ЛЕКСИЧЕСКИЕ ПРАВИЛА (Tokens)
// ----------------------------------------------------------------------------

// Ключевые слова
ЦЕЛ         : 'цел';        // целочисленный тип
ЛОГ         : 'лог';        // логический тип
СТР         : 'стр';        // строковый тип
ЕСЛИ        : 'если';
ТОГДА       : 'тогда';
ИНАЧЕЕСЛИ   : 'иначеесли';
ИНАЧЕ       : 'иначе';
ПОКА        : 'пока';
ВЫВЕСТИ     : 'вывести';
И           : 'и';
ИЛИ         : 'или';
ИСТИНА      : 'истина';
ЛОЖЬ        : 'ложь';

// Символы
LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
SEMICOLON   : ';';
COMMA       : ',';
ASSIGN      : '=';
PLUS        : '+';
MINUS       : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%'; 
LT          : '<';
GT          : '>';
LE          : '<=';
GE          : '>=';
EQ          : '==';
NEQ         : '!=';

// Идентификатор: русские/латинские буквы + _
IDENT
    : [а-яА-ЯёЁa-zA-Z_] [а-яА-ЯёЁa-zA-Z_0-9]*
    ;

// Целые числа
INT_NUMBER
    : [0-9]+
    ;

// Строка в двойных кавычках
STRING
    : '"' (~["\\] | '\\' .)* '"'  
    ;

// Пропуск пробелов и переводов строк
WS
    : [ \t\r\n]+ -> skip
    ;

// Многострочные комментарии
COMMENT
    : '/*' .*? '*/' -> skip
    ;

// Однострочные комментарии (C++-подобные)
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

// ----------------------------------------------------------------------------
// 2. СИНТАКСИЧЕСКИЕ ПРАВИЛА (Parser rules)
// ----------------------------------------------------------------------------

program
    : (globalStatement)* EOF
    ;

// "Глобальные" операторы (объявления и любые операторные конструкции)
globalStatement
    : varDeclaration
    | statement
    ;

// Объявление переменных: напр. "цел a, b; лог x; стр y;"
varDeclaration
    : (ЦЕЛ | ЛОГ | СТР) varList SEMICOLON
    ;

varList
    : IDENT (COMMA IDENT)*
    ;

// Операторы
statement
    : assignmentStatement
    | printStatement
    | ifStatement
    | whileStatement
    | blockStatement
    ;

// Присваивание: a = expr;
assignmentStatement
    : IDENT ASSIGN expr SEMICOLON
    ;

// Вывод: вывести(expr);
printStatement
    : ВЫВЕСТИ LPAREN expr RPAREN SEMICOLON
    ;

// Ветвление: если (expr) тогда { ... } иначеесли { ... } иначе { ... }
ifStatement
    : ЕСЛИ LPAREN expr RPAREN ТОГДА blockStatement (иначеЕслиPart)* (иначеPart)?
    ;

иначеЕслиPart
    : ИНАЧЕЕСЛИ LPAREN expr RPAREN ТОГДА blockStatement
    ;

// Факультативное иначе
иначеPart
    : ИНАЧЕ blockStatement
    ;

// Цикл пока (expr) { ... }
whileStatement
    : ПОКА LPAREN expr RPAREN blockStatement
    ;

// Блок: { statement* }
blockStatement
    : LBRACE (statement)* RBRACE
    ;

// Выражение
expr
    : orExpr
    ;

orExpr
    : andExpr (ИЛИ andExpr)*
    ;

andExpr
    : equalityExpr (И equalityExpr)*
    ;

equalityExpr
    : relationalExpr ( (EQ | NEQ) relationalExpr )*
    ;

relationalExpr
    : additiveExpr ((LT | GT | LE | GE | EQ | NEQ) additiveExpr)?
    ;

additiveExpr
    : multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*
    ;

multiplicativeExpr
    : atom ((MUL | DIV | MOD) atom)*
    ;

// atom — это базовый элемент: число, переменная, логическая константа, скобки
atom
    : INT_NUMBER
    | STRING
    | ИСТИНА
    | ЛОЖЬ
    | IDENT
    | LPAREN expr RPAREN
    ;
