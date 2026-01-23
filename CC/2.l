%{
#include <stdio.h>
#include <string.h>

int line_num = 1;
int col_num = 1;
int error_count = 0;

void update_column(int n) {
    col_num += n;
}

void print_token(const char *type, const char *lexeme) {
    printf("%-15s %-20s [Line %d, Col %d]\n", type, lexeme, line_num, col_num - (int)strlen(lexeme));
}
%}

%option noyywrap

DIGIT       [0-9]
LETTER      [a-zA-Z_]
ID          {LETTER}({LETTER}|{DIGIT})*
INTEGER     {DIGIT}+
FLOAT       {DIGIT}+\.{DIGIT}+
WHITESPACE  [ \t]

%%

    /* Keywords */
"int"       { print_token("KEYWORD", yytext); update_column(yyleng); }
"float"     { print_token("KEYWORD", yytext); update_column(yyleng); }
"if"        { print_token("KEYWORD", yytext); update_column(yyleng); }
"else"      { print_token("KEYWORD", yytext); update_column(yyleng); }
"while"     { print_token("KEYWORD", yytext); update_column(yyleng); }
"for"       { print_token("KEYWORD", yytext); update_column(yyleng); }
"return"    { print_token("KEYWORD", yytext); update_column(yyleng); }
"void"      { print_token("KEYWORD", yytext); update_column(yyleng); }

    /* Identifiers */
{ID}        { print_token("IDENTIFIER", yytext); update_column(yyleng); }

    /* Numbers */
{INTEGER}   { print_token("INTEGER", yytext); update_column(yyleng); }
{FLOAT}     { print_token("FLOAT", yytext); update_column(yyleng); }

    /* String Literals */
\"([^\\\"\n]|\\.)*\"  { 
    print_token("STRING", yytext); 
    update_column(yyleng); 
}

\"([^\\\"\n]|\\.)*$ {
    printf("LEXICAL ERROR: Unterminated string '%s' [Line %d, Col %d]\n", yytext, line_num, col_num);
    error_count++;
    update_column(yyleng);
}

    /* Single-line Comments */
"//".*      { print_token("COMMENT", yytext); update_column(yyleng); }

    /* Multi-line Comments */
"/*"([^*]|\*+[^*/])*\*+"/" { 
    int i;
    for (i = 0; i < yyleng; i++) {
        if (yytext[i] == '\n') {
            line_num++;
            col_num = 1;
        } else {
            col_num++;
        }
    }
    printf("COMMENT: %s\n", yytext);
}

"/*"([^*]|\*+[^*/])*$ {
    printf("LEXICAL ERROR: Unterminated comment starting at [Line %d, Col %d]\n", line_num, col_num);
    error_count++;
}

    /* Operators */
"+"         { print_token("OPERATOR", yytext); update_column(yyleng); }
"-"         { print_token("OPERATOR", yytext); update_column(yyleng); }
"*"         { print_token("OPERATOR", yytext); update_column(yyleng); }
"/"         { print_token("OPERATOR", yytext); update_column(yyleng); }
"="         { print_token("OPERATOR", yytext); update_column(yyleng); }
"=="        { print_token("OPERATOR", yytext); update_column(yyleng); }
"!="        { print_token("OPERATOR", yytext); update_column(yyleng); }
"<"         { print_token("OPERATOR", yytext); update_column(yyleng); }
">"         { print_token("OPERATOR", yytext); update_column(yyleng); }
"<="        { print_token("OPERATOR", yytext); update_column(yyleng); }
">="        { print_token("OPERATOR", yytext); update_column(yyleng); }
"&&"        { print_token("OPERATOR", yytext); update_column(yyleng); }
"||"        { print_token("OPERATOR", yytext); update_column(yyleng); }

    /* Delimiters */
";"         { print_token("DELIMITER", yytext); update_column(yyleng); }
","         { print_token("DELIMITER", yytext); update_column(yyleng); }
"("         { print_token("DELIMITER", yytext); update_column(yyleng); }
")"         { print_token("DELIMITER", yytext); update_column(yyleng); }
"{"         { print_token("DELIMITER", yytext); update_column(yyleng); }
"}"         { print_token("DELIMITER", yytext); update_column(yyleng); }

    /* Whitespace */
{WHITESPACE}+ { update_column(yyleng); }

    /* Newline */
\n          { line_num++; col_num = 1; }

    /* Lexical Errors */
.           { 
    printf("LEXICAL ERROR: Invalid character '%c' [Line %d, Col %d]\n", yytext[0], line_num, col_num);
    error_count++;
    update_column(1);
}

%%

int main() {
    printf("Input: Keywords and Identifiers\n");
    YY_BUFFER_STATE buf = yy_scan_string("int count if main");
    yylex();
    yy_delete_buffer(buf);
    printf("\n");
    
    printf("Input: Numbers and Strings\n");
    line_num = 1; col_num = 1;
    buf = yy_scan_string("123 45.67 \"hello world\"");
    yylex();
    yy_delete_buffer(buf);
    printf("\n");
    
    printf("Input: Single-Line Comment\n");
    line_num = 1; col_num = 1;
    buf = yy_scan_string("// This is a comment");
    yylex();
    yy_delete_buffer(buf);
    printf("\n");
    
    printf("Input: Multi-Line Comment\n");
    line_num = 1; col_num = 1;
    buf = yy_scan_string("/* Multi\nLine\nComment */");
    yylex();
    yy_delete_buffer(buf);
    printf("\n");
    
    printf("Input: Operators and Delimiters\n");
    line_num = 1; col_num = 1;
    buf = yy_scan_string("x = 10; if (y >= 5)");
    yylex();
    yy_delete_buffer(buf);
    printf("\n");
    
    printf("Input: Lexical Error\n");
    line_num = 1; col_num = 1;
    buf = yy_scan_string("int @invalid $ test");
    yylex();
    yy_delete_buffer(buf);
    printf("\n");
    
    printf("Input: Unterminated String Error\n");
    line_num = 1; col_num = 1;
    buf = yy_scan_string("\"unterminated string");
    yylex();
    yy_delete_buffer(buf);
    printf("\n");
    
    if (error_count > 0) {
        printf("\nTotal Lexical Errors: %d\n", error_count);
    }
    
    return 0;
}