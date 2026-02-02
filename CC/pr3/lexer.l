%{
#include <stdio.h>
int valid_count = 0;
int invalid_count = 0;
%}

%%
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}    { 
    printf("✓ Valid Email: %s\n", yytext); 
    valid_count++;
}

[A-Za-z0-9._%+-]+@[^ \t\n]+                       { 
    printf("✗ Invalid Email (missing/invalid domain): %s\n", yytext); 
    invalid_count++;
}

[^ \t\n@]+@                                        { 
    printf("✗ Invalid Email (incomplete): %s\n", yytext); 
    invalid_count++;
}

[ \t\n]+                                           { /* skip whitespace */ }

.                                                  { 
    printf("✗ Not an email: %s\n", yytext); 
    invalid_count++;
}

%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter emails (Ctrl+D to finish):\n");
    yylex();

    printf("Valid: %d\n", valid_count);
    printf("Invalid: %d\n", invalid_count);
    return 0;
}