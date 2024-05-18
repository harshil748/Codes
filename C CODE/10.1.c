#include <stdio.h>
#include <string.h>
struct BookDetail
{
  char title[100];
  char author[100];
  float amount;
};
void displayBookDetails(struct BookDetail book)
{
  printf("Book Title: %s\n", book.title);
  printf("Author Name: %s\n", book.author);
  printf("Amount: ₨%.2f\n", book.amount);
}
int main()
{
  struct BookDetail book1;
  printf("Enter Book Title: ");
  fgets(book1.title, sizeof(book1.title), stdin);
  printf("Enter Author Name: ");
  fgets(book1.author, sizeof(book1.author), stdin);
  printf("Enter Amount: ");
  scanf("%f", &book1.amount);
  displayBookDetails(book1);
  return 0;
}