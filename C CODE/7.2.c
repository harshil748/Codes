#include <stdio.h>
int main()
{
    int size1, size2;
    printf("Enter the size of the first array: ");
    scanf("%d", &size1);
    int arr1[size1];
    printf("Enter %d elements for the first array: ", size1);
    for (int i = 0; i < size1; i++)
    {
        scanf("%d", &arr1[i]);
    }
    printf("Enter the size of the second array: ");
    scanf("%d", &size2);
    int arr2[size2];
    printf("Enter %d elements for the second array: ", size2);
    for (int i = 0; i < size2; i++)
    {
        scanf("%d", &arr2[i]);
    }
    int mergedSize = size1 + size2;
    for (int i = 0; i < size1 - 1; i++)
    {
        for (int j = 0; j < size1 - i - 1; j++)
        {
            if (arr1[j] > arr1[j + 1])
            {
                int temp = arr1[j];
                arr1[j] = arr1[j + 1];
                arr1[j + 1] = temp;
            }
        }
    }
    for (int i = 0; i < size2 - 1; i++)
    {
        for (int j = 0; j < size2 - i - 1; j++)
        {
            if (arr2[j] > arr2[j + 1])
            {
                int temp = arr2[j];
                arr2[j] = arr2[j + 1];
                arr2[j + 1] = temp;
            }
        }
    }
    int mergedArr[mergedSize];
    int i = 0, j = 0, k = 0;
    while (i < size1 && j < size2)
    {
        if (arr1[i] <= arr2[j])
        {
            mergedArr[k] = arr1[i];
            i++;
        }
        else
        {
            mergedArr[k] = arr2[j];
            j++;
        }
        k++;
    }
    while (i < size1)
    {
        mergedArr[k] = arr1[i];
        i++;
        k++;
    }
    while (j < size2)
    {
        mergedArr[k] = arr2[j];
        j++;
        k++;
    }
    printf("Merged and sorted array: ");
    for (int i = 0; i < mergedSize; i++)
    {
        printf("%d ", mergedArr[i]);
    }
    return 0;
}