%{
#include <stdio.h>
#include <stdlib.h>

extern char line_buffer[];
int yylex(void);
void yyerror(const char *s);
%}

%token A B NL OTHER

%%
input
    : /* empty */
    | input line
    ;

line
    : pattern NL
      {
          printf("%s -> Valid\n", line_buffer);
      }
    | error NL
      {
                    printf("%s -> Invalid\n", line_buffer);
          yyerrok;
      }
    ;

pattern
    : A pattern B
    | A B
    ;
%%

void yyerror(const char *s)
{
    (void)s;
}

int main(void)
{
    return yyparse();
}