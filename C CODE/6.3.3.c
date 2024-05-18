#include <stdio.h>
int main()
{
    int n, i, j;
    char ch = 'A';
    printf("Enter the number of rows: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {

        for (j = 1; j <= n - i; j++)
        {
            printf("  ");
        }
        for (j = 1; j <= i; j++)
        {
            printf("%c ", ch++);
        }
        ch--;
        for (j = 1; j < i; j++)
        {
            printf("%c ", --ch);
        }
        printf("\n");
        ch = 'A';
    }
    return 0;
}