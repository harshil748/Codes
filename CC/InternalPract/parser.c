#include <stdio.h>
#include <string.h>

char input[100];
int i = 0;

void S()
{
    if (input[i] == '(')
    {
        i++;
        S();

        if (input[i] == ')')
        {
            i++;
            S();
        }
        else
        {
            printf("Invalid\n");
            return;
        }
    }
}

int main()
{
    printf("Enter expression:\n");
    scanf("%s", input);

    S();

    if (input[i] == '\0')
        printf("Valid expression\n");
    else
        printf("Invalid expression");

    return 0;
}