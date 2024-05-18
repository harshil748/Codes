#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n, *arr, sum = 0;
    float average;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL)
    {
        printf("Memory allocation failed!");
        return 1;
    }
    printf("Enter %d numbers:\n", n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    average = (float)sum / n;
    printf("Average of the numbers is: %.2f\n", average);
    free(arr);
    return 0;
}