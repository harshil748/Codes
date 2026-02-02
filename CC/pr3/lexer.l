 %{
#include <stdio.h>

int line = 1;
int col  = 1;

void advance() {
    col += yyleng;
}

void print_token(const char *type) {
    printf("<%s, \"%s\", line=%d, col=%d>\n",
           type, yytext, line, col);
}
%}

%x COMMENT

KEYWORD if|else|while|for|return|int|float|char|void
ID      [a-zA-Z_][a-zA-Z0-9_]*
INT     [0-9]+
FLOAT   [0-9]+\.[0-9]+
STRING  \"([^\\\n]|(\\.))*\"
OP      ">="|"<="|"=="|"!="|\+|\-|\*|/|=|\>|\<
DELIM   [(){};,]

%%
[\n]            { line++; col = 1; }
[ \t]+          { advance(); }

"//".*          { print_token("COMMENT"); advance(); }
"/*"            { BEGIN(COMMENT); advance(); }

<COMMENT>"*/"   { BEGIN(INITIAL); advance(); }
<COMMENT>[\n]   { line++; col = 1; }
<COMMENT>.      { advance(); }

{KEYWORD}       { print_token("KEYWORD"); advance(); }
{FLOAT}         { print_token("FLOAT"); advance(); }
{INT}           { print_token("INT"); advance(); }
{STRING}        { print_token("STRING"); advance(); }
{ID}            { print_token("IDENTIFIER"); advance(); }
{OP}            { print_token("OPERATOR"); advance(); }
{DELIM}         { print_token("DELIMITER"); advance(); }

. {
    printf("Lexical Error: '%s' at line %d col %d\n",
           yytext, line, col);
    advance();
}
%%

int yywrap() {
    return 1;
}

