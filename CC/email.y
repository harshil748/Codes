/* 
 * EMAIL VALIDATION USING FLEX AND YACC
 * 
 * This file demonstrates email validation using:
 * 1. Flex (.l) - Lexical analyzer - Tokenizes input
 * 2. Yacc (.y) - Parser generator - Defines grammar rules
 * 
 * The approach:
 * - Flex breaks the email into tokens (LOCALPART, @, DOMAIN, DOT, TLD)
 * - Yacc uses grammar rules to validate the token sequence
 * - Valid pattern: LOCALPART @ DOMAIN . TLD
 */

%{
#include <stdio.h>
#include <string.h>

int valid_email = 1;
extern int yylex();
extern void yyerror(const char *s);

%}

%union {
    char *str;
}

%token <str> LOCALPART DOMAIN TLD
%token AT DOT

%%

email:
    LOCALPART AT DOMAIN DOT TLD
    {
        printf("%s@%s.%s -> Valid Email\n", $1, $3, $5);
        valid_email = 1;
    }
    | LOCALPART AT DOMAIN DOT DOMAIN DOT TLD
    {
        /* Support subdomains */
        printf("%s@%s.%s.%s -> Valid Email\n", $1, $3, $5, $7);
        valid_email = 1;
    }
    | error
    {
        printf("Invalid Email\n");
        valid_email = 0;
    }
    ;

%%

void yyerror(const char *s) {
    valid_email = 0;
}

int main() {
    printf("╔═══════════════════════════════════════════════════════╗\n");
    printf("║   EMAIL VALIDATION USING FLEX + YACC                 ║\n");
    printf("╚═══════════════════════════════════════════════════════╝\n\n");
    
    yyparse();
    return 0;
}
