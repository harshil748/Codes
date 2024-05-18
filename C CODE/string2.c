#include <stdio.h>
#include <string.h>
int main()
{
    char str1[100], str2[100], result[200];
    int choice;
    printf("Enter the string 1: ");
    scanf("%s", str1);
    printf("Enter the string 2: ");
    scanf("%s", str2);
    do
    {
        printf("1. Find the length of string\n");
        printf("2. Reverse the string\n");
        printf("3. Compare two strings\n");
        printf("4. Copy one string into another\n");
        printf("5. Concatenate two strings\n");
        printf("6. Exit\n");
        printf("Enter your choice\n");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("Length of the first string is %ld\n", strlen(str1));
            printf("Length of the senond string is %ld\n", strlen(str2));
            break;
        case 2:
            printf("Reverse of the first string is : ");
            for (int i = strlen(str1) - 1; i >= 0; i--)
            {
                printf("%c", str1[i]);
            }
            printf("\n");
            break;
        case 3:
            if (strcmp(str1, str2) == 0)
            {
                printf("The strings are equal\n");
            }
            else
            {
                printf("The strings are not equal\n");
            }
            break;
        case 4:
            strcpy(result, str1);
            printf("Copy of the first string into the result: %s\n", result);
            break;
        case 5:
            strcpy(result, str1);
            strcat(result, str2);
            printf("Concatenated strings: %s\n", result);
            break;
        case 6:
            printf("Exiting the program\n");
            break;
        default:
            printf("Invalid choice\n");
        }
    } while (choice != 6);
    return 0;
}