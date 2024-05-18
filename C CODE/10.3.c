#include <stdio.h>
struct Address
{
    char street[100];
    char city[50];
    char state[50];
    char zip[10];
};
struct Employee
{
    int age;
    char name[100];
    struct Address address;
    float salary;
};
int main()
{
    struct Employee employee;
    printf("Enter Employee Details:\n");
    printf("Age: ");
    scanf("%d", &employee.age);
    printf("Name: ");
    scanf(" %s", employee.name);
    printf("Address:\n");
    printf("Street: ");
    scanf(" %s", employee.address.street);
    printf("City: ");
    scanf(" %s", employee.address.city);
    printf("State: ");
    scanf(" %s", employee.address.state);
    printf("ZIP Code: ");
    scanf(" %s", employee.address.zip);
    printf("Salary: ");
    scanf("%f", &employee.salary);
    printf("\nEmployee Details:\n");
    printf("Age: %d\n", employee.age);
    printf("Name: %s\n", employee.name);
    printf("\nAddress:\n");
    printf("Street: %s\n", employee.address.street);
    printf("City: %s\n", employee.address.city);
    printf("State: %s\n", employee.address.state);
    printf("ZIP Code: %s\n", employee.address.zip);
    printf("Salary: ₨ %.2f\n", employee.salary);
    return 0;
}