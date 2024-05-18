#include <stdio.h>
int main()
{
    char str1[100], str2[100];
    int choice;
    printf("Enter string 1: ");
    scanf("%s", str1);
    printf("Enter string 2: ");
    scanf("%s", str2);
    do
    {
        printf("Choose an option:\n");
        printf("1.Length of string 1\n");
        printf("2.Length of string 2\n");
        printf("3.Reverse string 1\n");
        printf("4.Reverse string 2\n");
        printf("5.Compare strings 1 and 2\n");
        printf("6.Copy string 1 into string 2\n");
        printf("7.Copy string 2 into string 1\n");
        printf("8.Concatenate strings 1 and 2\n");
        printf("9.Exit.\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
        {
            int length = 0;
            while (str1[length] != '\0')
            {
                length++;
            }
            printf("Length of string 1:%d\n", length);
        }
        break;
        case 2:
        {
            int length = 0;
            while (str2[length] != '\0')
            {
                length++;
            }
            printf("Length of string 2:%d\n", length);
        }
        break;
        case 3:
        {
            int start = 0;
            int end = 0;
            while (str1[end] != '\0')
            {
                end++;
            }
            end--;
            while (start < end)
            {
                char temp = str1[start];
                str1[start] = str1[end];
                str1[end] = temp;
                start++;
                end--;
            }
            printf("Reversed string 1: %s\n", str1);
        }
        break;
        case 4:
        {
            int start = 0;
            int end = 0;
            while (str2[end] != '\0')
            {
                end++;
            }
            end--;
            while (start < end)
            {
                char temp = str2[start];
                str2[start] = str2[end];
                str2[end] = temp;
                start++;
                end--;
            }
            printf("Reversed string 2: %s\n", str2);
        }
        break;
        case 5:
        {
            int equal = 1;
            int i = 0;
            while (str1[i] != '\0' || str2[i] != '\0')
            {
                if (str1[i] != str2[i])
                {
                    equal = 0;
                    break;
                }
                i++;
            }
            if (equal)
            {
                printf("Strings are equal.\n");
            }
            else
            {
                printf("Strings are not equal.\n");
            }
        }
        break;
        case 6:
        {
            int i = 0;
            while (str1[i] != '\0')
            {
                str2[i] = str1[i];
                i++;
            }
            str2[i] = '\0';
            printf("String 1 copied into string 2: %s\n", str2);
        }
        break;
        case 7:
        {
            int i = 0;
            while (str2[i] != '\0')
            {
                str1[i] = str2[i];
                i++;
            }
            str2[i] = '\0';
            printf("String 2 copied into string 1: %s\n", str1);
        }
        break;
        case 8:
        {
            int i = 0;
            while (str1[i] != '\0')
            {
                i++;
            }
            int j = 0;
            while (str2[j] != '\0')
            {
                str1[i] = str2[j];
                i++;
                j++;
            }
            str1[i] = '\0';
            printf("Concatenated string: %s\n", str1);
        }
        break;
        case 9:
        {
            printf("\nExiting the program.");
        }
        break;
        default:
            printf("Invalid choice.\n");
        }
    } while (choice != 9);
    return 0;
}