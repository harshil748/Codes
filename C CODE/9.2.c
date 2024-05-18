#include <stdio.h>
#include <math.h>
float calculate_area(float a, float b, float c)
{
  float s = (a + b + c) / 2;
  float area = sqrt(s * (s - a) * (s - b) * (s - c));
  return area;
}
void verify_triangle()
{
  float a, b, c;
  printf("Enter the length of side a: ");
  scanf("%f", &a);
  printf("Enter the length of side b: ");
  scanf("%f", &b);
  printf("Enter the length of side c: ");
  scanf("%f", &c);
  if (a + b > c && a + c > b && b + c > a)
  {
    printf("Triangle is valid.\n");
    float area = calculate_area(a, b, c);
    printf("Area of the triangle is %.2f\n", area);
  }
  else
  {
    printf("Triangle is not valid.\n");
  }
}
int main()
{
  verify_triangle();
  return 0;
}