#include <stdio.h>
void decimaltoBinary(int n)
{
    if (n > 0)
    {
        decimaltoBinary(n / 2);
        printf("%d", n % 2);
    }
}
int main()
{
    int dn;
    printf("Enter a positive integer: ");
    scanf("%d", &dn);
    if (dn < 0)
    {
        printf("Please enter a positive integer.\n");
    }
    else if (dn == 0)
    {
        printf("Binary equivalent: 0\n");
    }
    else
    {
        printf("Binary equivalent: ");
        decimaltoBinary(dn);
        printf("\n");
    }
    return 0;
}