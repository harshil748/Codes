#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef enum
{
    TOK_ID,
    TOK_NUM,
    TOK_OP,
    TOK_LP,
    TOK_RP,
    TOK_ASSIGN,
    TOK_END
} TokType;

typedef struct
{
    TokType type;
    char text[64];
} Token;

#define MAX_TOK 256

static int is_id_start(char c) { return isalpha((unsigned char)c) || c == '_'; }
static int is_id_char(char c) { return isalnum((unsigned char)c) || c == '_'; }

static int tokenize(const char *s, Token toks[], int *n)
{
    int i = 0, p = 0;
    while (s[i])
    {
        if (isspace((unsigned char)s[i]))
        {
            i++;
            continue;
        }
        if (is_id_start(s[i]))
        {
            int j = 0;
            while (s[i] && is_id_char(s[i]) && j < 63)
                toks[p].text[j++] = s[i++];
            toks[p].text[j] = '\0';
            toks[p].type = TOK_ID;
            p++;
            continue;
        }
        if (isdigit((unsigned char)s[i]))
        {
            int j = 0;
            while (s[i] && isdigit((unsigned char)s[i]) && j < 63)
                toks[p].text[j++] = s[i++];
            toks[p].text[j] = '\0';
            toks[p].type = TOK_NUM;
            p++;
            continue;
        }
        if (s[i] == '=')
        {
            toks[p].type = TOK_ASSIGN;
            toks[p].text[0] = '=';
            toks[p].text[1] = '\0';
            p++;
            i++;
            continue;
        }
        if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/')
        {
            toks[p].type = TOK_OP;
            toks[p].text[0] = s[i];
            toks[p].text[1] = '\0';
            p++;
            i++;
            continue;
        }
        if (s[i] == '(')
        {
            toks[p].type = TOK_LP;
            toks[p].text[0] = '(';
            toks[p].text[1] = '\0';
            p++;
            i++;
            continue;
        }
        if (s[i] == ')')
        {
            toks[p].type = TOK_RP;
            toks[p].text[0] = ')';
            toks[p].text[1] = '\0';
            p++;
            i++;
            continue;
        }
        return 0; /* unknown char */
    }
    toks[p].type = TOK_END;
    toks[p].text[0] = '\0';
    *n = p + 1;
    return 1;
}

static int prec(char op)
{
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return 0;
}

int main(void)
{
    char line[1024];
    printf("Enter assignment expression (e.g. x = (a + b) * (c - d) + e * f / g):\n");
    if (!fgets(line, sizeof(line), stdin))
        return 0;

    Token toks[MAX_TOK];
    int ntoks = 0;
    if (!tokenize(line, toks, &ntoks))
    {
        printf("Tokenize error.\n");
        return 1;
    }

    /* Expect ID ASSIGN ... */
    if (toks[0].type != TOK_ID || toks[1].type != TOK_ASSIGN)
    {
        printf("Input must be assignment of form id = expr\n");
        return 1;
    }
    char lhs[64];
    strcpy(lhs, toks[0].text);

    /* Shunting-yard to produce postfix tokens (we store text in array) */
    Token output[MAX_TOK];
    int outc = 0;
    Token opstack[MAX_TOK];
    int opst = 0;

    for (int i = 2; i < ntoks; i++)
    {
        Token t = toks[i];
        if (t.type == TOK_ID || t.type == TOK_NUM)
        {
            output[outc++] = t;
        }
        else if (t.type == TOK_OP)
        {
            while (opst > 0 && opstack[opst - 1].type == TOK_OP)
            {
                char o1 = opstack[opst - 1].text[0];
                char o2 = t.text[0];
                if ((prec(o1) > prec(o2)) || (prec(o1) == prec(o2)))
                {
                    output[outc++] = opstack[--opst];
                }
                else
                    break;
            }
            opstack[opst++] = t;
        }
        else if (t.type == TOK_LP)
        {
            opstack[opst++] = t;
        }
        else if (t.type == TOK_RP)
        {
            int found = 0;
            while (opst > 0)
            {
                Token tt = opstack[--opst];
                if (tt.type == TOK_LP)
                {
                    found = 1;
                    break;
                }
                output[outc++] = tt;
            }
            if (!found)
            {
                printf("Mismatched parentheses\n");
                return 1;
            }
        }
    }
    while (opst > 0)
    {
        if (opstack[opst - 1].type == TOK_LP || opstack[opst - 1].type == TOK_RP)
        {
            printf("Mismatched parentheses\n");
            return 1;
        }
        output[outc++] = opstack[--opst];
    }

    /* Generate quadruples from postfix */
    char stack[MAX_TOK][64];
    int sp = 0;
    struct Quad
    {
        char op[8];
        char arg1[64];
        char arg2[64];
        char res[64];
    } quads[512];
    int qn = 0;
    int tempcnt = 0;

    for (int i = 0; i < outc; i++)
    {
        Token t = output[i];
        if (t.type == TOK_ID || t.type == TOK_NUM)
        {
            strcpy(stack[sp++], t.text);
        }
        else if (t.type == TOK_OP)
        {
            if (sp < 2)
            {
                printf("Error: insufficient operands\n");
                return 1;
            }
            char right[64], left[64];
            strcpy(right, stack[--sp]);
            strcpy(left, stack[--sp]);
            tempcnt++;
            char resname[64];
            sprintf(resname, "t%d", tempcnt);
            strcpy(quads[qn].op, t.text);
            strcpy(quads[qn].arg1, left);
            strcpy(quads[qn].arg2, right);
            strcpy(quads[qn].res, resname);
            qn++;
            strcpy(stack[sp++], resname);
        }
    }
    if (sp != 1)
    {
        printf("Error: malformed expression\n");
        return 1;
    }
    /* final assignment */
    strcpy(quads[qn].op, "=");
    strcpy(quads[qn].arg1, stack[--sp]);
    strcpy(quads[qn].arg2, "-");
    strcpy(quads[qn].res, lhs);
    qn++;

    /* Print quadruples */
    printf("\nQuadruples:\n");
    printf("%-4s | %-10s | %-10s | %-10s\n", "Op", "Arg1", "Arg2", "Result");
    printf("-----------------------------------------------\n");
    for (int i = 0; i < qn; i++)
    {
        printf("%-4s | %-10s | %-10s | %-10s\n", quads[i].op, quads[i].arg1, quads[i].arg2, quads[i].res);
    }

    return 0;
}
