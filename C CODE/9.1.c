#include <stdio.h>
//(i) No arguments passed and no return value
void checkFactorialNoArgsNoReturn()
{
  int num, i, fact = 1;
  printf("Enter a number: ");
  scanf("%d", &num);
  for (i = 1; i <= num; i++)
  {
    fact *= i;
    if (fact == num)
    {
      printf("%d is a factorial.\n", num);
      return;
    }
    if (fact > num)
    {
      printf("%d is not a factorial.\n", num);
      return;
    }
  }
  printf("%d is not a factorial.\n", num);
}
// (ii) No arguments passed but a return value.
int checkFactorialNoArgsWithReturn()
{
  int num, i, fact = 1;
  printf("Enter a number: ");
  scanf("%d", &num);
  for (i = 1; i <= num; i++)
  {
    fact *= i;
    if (fact == num)
    {
      return 1;
    }
    if (fact > num)
    {
      return 0;
    }
  }
  return 0;
}
// (iii) Argument passed but no return value.
void checkFactorialWithArgNoReturn(int num)
{
  int i, fact = 1;
  for (i = 1; i <= num; i++)
  {
    fact *= i;
    if (fact == num)
    {
      printf("%d is a factorial.\n", num);
      return;
    }
    if (fact > num)
    {
      printf("%d is not a factorial.\n", num);
      return;
    }
  }
  printf("%d is not a factorial.\n", num);
}
// (iv) Argument passed and a return value.
int checkFactorialWithArgAndReturn(int num)
{
  int i, fact = 1;
  for (i = 1; i <= num; i++)
  {
    fact *= i;
    if (fact == num)
    {
      return 1;
    }
    if (fact > num)
    {
      return 0;
    }
  }
  return 0;
}
int main()
{
  int num;
  // (i) No arguments passed and no return value.
  checkFactorialNoArgsNoReturn();
  // (ii) No arguments passed but a return value.
  if (checkFactorialNoArgsWithReturn() == 1)
  {
    printf("Using (ii): It's a factorial.\n");
  }
  else
  {
    printf("Using (ii): It's not a factorial.\n");
  }
  //(iii) Argument passed but no return value.
  printf("Enter a number: ");
  scanf("%d", &num);
  checkFactorialWithArgNoReturn(num);
  //(iv) Argument passed and a return value.
  printf("Enter a number: ");
  scanf("%d", &num);
  if (checkFactorialWithArgAndReturn(num) == 1)
  {
    printf("Using (iv): It's a factorial.\n");
  }
  else
  {
    printf("Using (iv): It's not a factorial.\n");
  }
  return 0;
}