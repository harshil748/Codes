%{
#include <stdio.h>
%}

%option noyywrap

%%
[0-9]+          
.|
\n              { ECHO; }
%%

int main(void) {
    yylex();
    return 0;
}
