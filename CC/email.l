%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int valid_email = 1;
char local_part[256];
char domain_part[256];
char tld_part[256];

void print_result(const char *email) {
    printf("%s -> ", email);
    if (valid_email) {
        printf("Valid Email\n");
    } else {
        printf("Invalid Email\n");
    }
}

%}

%option noyywrap

DIGIT           [0-9]
LETTER          [A-Za-z]

%%

[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}  {
    valid_email = 1;
    printf("%s -> Valid Email\n", yytext);
}

.+  {
    valid_email = 0;
    printf("%s -> Invalid Email\n", yytext);
}

\n  { /* Skip newlines */ }

%%

int main() {
    printf("╔═══════════════════════════════════════════════════════╗\n");
    printf("║   EMAIL VALIDATION USING FLEX + YACC                 ║\n");
    printf("║                                                       ║\n");
    printf("║   Enter email addresses (one per line)                ║\n");
    printf("║   Ctrl+D to exit                                      ║\n");
    printf("╚═══════════════════════════════════════════════════════╝\n\n");
    
    yylex();
    return 0;
}
