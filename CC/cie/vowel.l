%{
#include<stdio.h>
int count=0;
%}

%%
[aeiouAEIOU] { count++; }
. ;
\n { printf("Total Vowels: %d\n",count); count=0; }
%%

int yywrap()
{
return 1;
}

int main()
{
yylex();
return 0;
}