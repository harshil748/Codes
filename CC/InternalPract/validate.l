%{
#include<stdio.h>
#include<string.h>
int a=0,b=0,c=0;
%}

%%

a {a++;}
b {b++;}
c {c++;}
\n {
if(a>0 && b>0 && c>0)
printf("Valid string\n");
else
printf("Invalid string\n");

a=b=c=0;
}

. ;

%%

int yywrap()
{
return 1;
}

int main()
{
printf("Enter string:\n");
yylex();
return 0;
}