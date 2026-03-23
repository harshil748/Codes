#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

/* Stack for operators */
char stack[MAX][20];
int top = -1;

/* Structures */
typedef struct
{
    char op[10], arg1[20], arg2[20], result[20];
} Quadruple;

typedef struct
{
    char op[10], arg1[20], arg2[20];
} Triple;

Quadruple quad[MAX];
Triple triple[MAX];
int qIndex = 0, tIndex = 0, tempCount = 1;

/* Push to stack */
void push(char *val)
{
    strcpy(stack[++top], val);
}

/* Pop from stack */
char *pop(void)
{
    return stack[top--];
}

/* Check precedence */
int precedence(char *op)
{
    if (strcmp(op, "+") == 0 || strcmp(op, "-") == 0)
        return 1;
    if (strcmp(op, "*") == 0 || strcmp(op, "/") == 0)
        return 2;
    return 0;
}

/* Check if operator */
int isOperator(char *c)
{
    return (!strcmp(c, "+") || !strcmp(c, "-") || !strcmp(c, "*") || !strcmp(c, "/"));
}

/* Generate new temp */
void newTemp(char *temp)
{
    sprintf(temp, "t%d", tempCount++);
}

/* Add Quadruple */
void addQuad(char *op, char *arg1, char *arg2, char *res)
{
    strcpy(quad[qIndex].op, op);
    strcpy(quad[qIndex].arg1, arg1);
    strcpy(quad[qIndex].arg2, arg2);
    strcpy(quad[qIndex].result, res);
    qIndex++;
}

/* Add Triple */
void addTriple(char *op, char *arg1, char *arg2)
{
    strcpy(triple[tIndex].op, op);
    strcpy(triple[tIndex].arg1, arg1);
    strcpy(triple[tIndex].arg2, arg2);
    tIndex++;
}

/* Convert infix to postfix (tokens separated by space) */
void infixToPostfix(char exp[][20], int n, char output[][20], int *outSize)
{
    int k = 0;
    for (int i = 0; i < n; i++)
    {
        if (isalnum(exp[i][0]))
        {
            strcpy(output[k++], exp[i]);
        }
        else if (strcmp(exp[i], "(") == 0)
        {
            push(exp[i]);
        }
        else if (strcmp(exp[i], ")") == 0)
        {
            while (top != -1 && strcmp(stack[top], "(") != 0)
            {
                strcpy(output[k++], pop());
            }
            pop(); /* remove "(" */
        }
        else
        {
            while (top != -1 && precedence(stack[top]) >= precedence(exp[i]))
            {
                strcpy(output[k++], pop());
            }
            push(exp[i]);
        }
    }

    while (top != -1)
    {
        strcpy(output[k++], pop());
    }
    *outSize = k;
}

/* Generate TAC, Quad, Triple */
void generateCode(char postfix[][20], int n)
{
    char evalStack[MAX][20];
    int eTop = -1;

    for (int i = 0; i < n; i++)
    {
        if (!isOperator(postfix[i]))
        {
            strcpy(evalStack[++eTop], postfix[i]);
        }
        else
        {
            char op2[20], op1[20], temp[20];
            strcpy(op2, evalStack[eTop--]);
            strcpy(op1, evalStack[eTop--]);
            newTemp(temp);

            /* TAC */
            printf("%s = %s %s %s\n", temp, op1, postfix[i], op2);

            /* Quad */
            addQuad(postfix[i], op1, op2, temp);

            /* Triple */
            addTriple(postfix[i], op1, op2);

            strcpy(evalStack[++eTop], temp);
        }
    }
}

/* Print Quadruples */
void printQuad(void)
{
    printf("\nQuadruples:\n");
    printf("Op\tArg1\tArg2\tResult\n");
    for (int i = 0; i < qIndex; i++)
    {
        printf("%s\t%s\t%s\t%s\n", quad[i].op, quad[i].arg1, quad[i].arg2, quad[i].result);
    }
}

/* Print Triples */
void printTriple(void)
{
    printf("\nTriples:\n");
    printf("Index\tOp\tArg1\tArg2\n");
    for (int i = 0; i < tIndex; i++)
    {
        printf("%d\t%s\t%s\t%s\n", i, triple[i].op, triple[i].arg1, triple[i].arg2);
    }
}

int main(void)
{
    /* Tokenized expression:
       ((quiz1 + quiz2)/2 * 0.2) + ((assignment1 + assignment2 * 2)/3 * 0.4)
    */
    char exp[][20] = {
        "(", "(", "quiz1", "+", "quiz2", ")", "/", "2", "*", "0.2", ")", "+",
        "(", "(", "assignment1", "+", "assignment2", "*", "2", ")", "/", "3", "*", "0.4", ")"};

    int n = (int)(sizeof(exp) / sizeof(exp[0]));
    char postfix[MAX][20];
    int postSize;

    infixToPostfix(exp, n, postfix, &postSize);
    printf("Three Address Code (TAC):\n");
    generateCode(postfix, postSize);
    printQuad();
    printTriple();

    return 0;
}