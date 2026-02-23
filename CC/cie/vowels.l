%{
#include <stdio.h>

static int vowel_count = 0;
%}

%option noyywrap

%%
[AEIOUaeiou]    { vowel_count++; }
.|
\n              {  }
%%

int main(void) {
    yylex();
    printf("Total Vowels: %d\n", vowel_count);
    return 0;
}
