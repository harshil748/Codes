#include <stdio.h>
int main()
{
    int numbers[25];
    int positiveCount = 0, negativeCount = 0, evenCount = 0, oddCount = 0;
    printf("Enter 25 numbers:\n");
    for (int i = 0; i < 25; i++)
    {
        scanf("%d", &numbers[i]);
    }
    for (int i = 0; i < 25; i++)
    {
        if (numbers[i] > 0)
        {
            positiveCount++;
        }
        else if (numbers[i] < 0)
        {
            negativeCount++;
        }
        if (numbers[i] % 2 == 0)
        {
            evenCount++;
        }
        else
        {
            oddCount++;
        }
    }
    printf("Positive numbers: %d\n", positiveCount);
    printf("Negative numbers: %d\n", negativeCount);
    printf("Even numbers: %d\n", evenCount);
    printf("Odd numbers: %d\n", oddCount);
    return 0;
}