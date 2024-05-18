#include <stdio.h>
#include <math.h>
int main()
{
    int choice;
    do
    {
        printf("Menu:\n");
        printf("1.Prime or not.\n");
        printf("2.Amstrong or not\n");
        printf("3.Perfect number or not\n");
        printf("4.Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
        {
            int n;
            printf("Enter a number: ");
            scanf("%d", &n);
            int isprime = 1;
            if (n <= 1)
            {
                isprime = 0;
            }
            else
            {
                for (int i = 2; i <= sqrt(n); i++)
                {
                    if (n % i == 0)
                    {
                        isprime = 0;
                        break;
                    }
                }
            }
            if (isprime)
            {
                printf("%d is a prime number.\n", n);
            }
            else
            {
                printf("%d is not a prime number.\n", n);
            }
            break;
        }
        case 2:
        {
            int an, on, re, result = 0;
            printf("Enter a number: ");
            scanf("%d", &an);
            on = an;
            while (on != 0)
            {
                re = on % 10;
                result += pow(re, 3);
                on /= 10;
            }
            if (result == an)
            {
                printf("%d is an Armstrong number.\n", an);
            }
            else
            {
                printf("%d is not an Armstrong number.\n", an);
            }
            break;
        }
        case 3:
        {
            int pn, d = 1, s = 0;
            printf("Enter a number: ");
            scanf("%d", &pn);
            do
            {
                if (pn % d == 0)
                {
                    s += d;
                }
                d++;
            } while (d < pn);
            if (s == pn)
            {
                printf("%d is a perfect number.\n", pn);
            }
            else
            {
                printf("%d is not a perfect number.\n", pn);
            }
            break;
        }
        case 4:
        {
            printf("Exiting the program.\n");
            break;
        }
        default:
        {
            printf("Invalid choice. Please try again.\n");
            break;
        }
        }
    } while (choice != 4);
    return 0;
}