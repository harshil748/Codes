#include <stdio.h>
#include <string.h>
#include <ctype.h>

int line = 1, col = 1;

void tokenize(char *input) {
    int i = 0;
    char token[100];
    int tokenIndex = 0;
    
    while (input[i] != '\0') {
        if (input[i] == ' ' || input[i] == '\t') {
            col++;
            i++;
            continue;
        }
        
        if (input[i] == '\n') {
            line++;
            col = 1;
            i++;
            continue;
        }
        
        if (input[i] == '/' && input[i+1] == '/') {
            printf("COMMENT: //");
            i += 2;
            col += 2;
            while (input[i] != '\n' && input[i] != '\0') {
                printf("%c", input[i]);
                i++;
                col++;
            }
            printf("\n");
            continue;
        }
        
        if (input[i] == '/' && input[i+1] == '*') {
            printf("COMMENT: /*");
            i += 2;
            col += 2;
            while (!(input[i] == '*' && input[i+1] == '/') && input[i] != '\0') {
                printf("%c", input[i]);
                if (input[i] == '\n') {
                    line++;
                    col = 1;
                } else {
                    col++;
                }
                i++;
            }
            if (input[i] == '*' && input[i+1] == '/') {
                printf("*/\n");
                i += 2;
                col += 2;
            }
            continue;
        }
        
        if (input[i] == '"') {
            tokenIndex = 0;
            token[tokenIndex++] = input[i];
            i++;
            col++;
            while (input[i] != '"' && input[i] != '\0') {
                token[tokenIndex++] = input[i];
                i++;
                col++;
            }
            if (input[i] == '"') {
                token[tokenIndex++] = input[i];
                i++;
                col++;
            }
            token[tokenIndex] = '\0';
            printf("STRING: %s\n", token);
            continue;
        }
        
        if (isdigit(input[i])) {
            tokenIndex = 0;
            while (isdigit(input[i]) || input[i] == '.') {
                token[tokenIndex++] = input[i];
                i++;
                col++;
            }
            token[tokenIndex] = '\0';
            printf("NUMBER: %s\n", token);
            continue;
        }
        
        if (isalpha(input[i]) || input[i] == '_') {
            tokenIndex = 0;
            while (isalnum(input[i]) || input[i] == '_') {
                token[tokenIndex++] = input[i];
                i++;
                col++;
            }
            token[tokenIndex] = '\0';
            
            if (strcmp(token, "int") == 0 || strcmp(token, "if") == 0 || 
                strcmp(token, "else") == 0 || strcmp(token, "while") == 0 ||
                strcmp(token, "return") == 0 || strcmp(token, "for") == 0) {
                printf("KEYWORD: %s\n", token);
            } else {
                printf("IDENTIFIER: %s\n", token);
            }
            continue;
        }
        
        if (strchr("+-*/=<>!&|", input[i])) {
            printf("OPERATOR: %c\n", input[i]);
            i++;
            col++;
            continue;
        }
        
        if (strchr("();{},", input[i])) {
            printf("DELIMITER: %c\n", input[i]);
            i++;
            col++;
            continue;
        }
        
        printf("ERROR: Invalid character '%c'\n", input[i]);
        i++;
        col++;
    }
}

int main() {
    printf("Input: int count if main\n");
    line = 1; col = 1;
    tokenize("int count if main");
    printf("\n");
    
    printf("Input: 123 45.67 \"hello world\"\n");
    line = 1; col = 1;
    tokenize("123 45.67 \"hello world\"");
    printf("\n");
    
    printf("Input: // This is a comment\n");
    line = 1; col = 1;
    tokenize("// This is a comment");
    printf("\n");
    
    printf("Input: /* Multi Line Comment */\n");
    line = 1; col = 1;
    tokenize("/* Multi\nLine\nComment */");
    printf("\n");
    
    printf("Input: int x = 10;\n");
    line = 1; col = 1;
    tokenize("int x = 10;");
    printf("\n");
    
    printf("Input: int @invalid\n");
    line = 1; col = 1;
    tokenize("int @invalid");
    
    return 0;
}