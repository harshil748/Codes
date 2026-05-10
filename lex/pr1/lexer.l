%{
#include "parser.tab.h"
#include <stdio.h>
#include <string.h>

char line_buffer[1024];
int line_length = 0;
%}

%%
[a]             { if (line_length < (int)sizeof(line_buffer) - 1) line_buffer[line_length++] = yytext[0]; return A; }
[b]             { if (line_length < (int)sizeof(line_buffer) - 1) line_buffer[line_length++] = yytext[0]; return B; }
\r              { /* ignore Windows CR */ }
\n              { line_buffer[line_length] = '\0'; line_length = 0; return NL; }
[ \t]+          { /* ignore spacing */ }
.               { if (line_length < (int)sizeof(line_buffer) - 1) line_buffer[line_length++] = yytext[0]; return OTHER; }
%%

int yywrap(void)
{
    return 1;
}