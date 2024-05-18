#include <stdio.h>
#include <string.h>
struct library
{
    int acc_no;
    char title[20];
    char author_name[20];
    int book_price;
    int flag;
};
int main()
{
    struct library s[3];
    int i;
    printf("Enter book details:\n");
    for (i = 0; i < 3; i++)
    {
        printf("Acc No: ");
        scanf("%d", &s[i].acc_no);
        getchar();

        printf("Title: ");
        fgets(s[i].title, sizeof(s[i].title), stdin);
        s[i].title[strcspn(s[i].title, "\n")] = '\0';
        printf("Author Name: ");
        fgets(s[i].author_name, sizeof(s[i].author_name), stdin);
        s[i].author_name[strcspn(s[i].author_name, "\n")] = '\0';
        printf("Book Price: ");
        scanf("%d", &s[i].book_price);
        getchar();
        printf("Flag (1 for issued, 0 for not issued): ");
        scanf("%d", &s[i].flag);
        getchar();
    }
    printf("\nBook Details:\n");
    for (i = 0; i < 3; i++)
    {
        printf("Acc No: %d\n", s[i].acc_no);
        printf("Title: %s\n", s[i].title);
        printf("Author Name: %s\n", s[i].author_name);
        printf("Book Price: %d\n", s[i].book_price);
        if (s[i].flag == 1)
        {
            printf("Status: Your book is issued\n");
        }
        else
        {
            printf("Status: Your book is not issued\n");
        }
        printf("\n");
    }
    return 0;
}