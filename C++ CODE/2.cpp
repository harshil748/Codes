#include <iostream>
#include <map>
#include <string>
using namespace std;
struct Employee
{
    string name;
    string qualification;
    double experience;
    string contactNumber;
};
map<int, Employee> employees;
void addEmployee()
{
    int id;
    string name;
    string qualification;
    double experience;
    string contactNumber;
    cout << "Enter Employee ID: ";
    cin >> id;
    cin.ignore();
    cout << "Enter Employee Name: ";
    getline(cin, name);
    cout << "Enter Qualification: ";
    cin >> qualification;
    cout << "Enter Experience: ";
    cin >> experience;
    cout << "Enter Contact Number: ";
    cin >> contactNumber;
    Employee newEmployee = {name, qualification, experience, contactNumber};
    employees[id] = newEmployee;
}
void getEmployeeDetails(int id)
{
    if (employees.find(id) != employees.end())
    {
        cout << "-----------------------------------\n";
        cout << "Employee Name       : " << employees[id].name << "\n";
        cout << "Qualification       : " << employees[id].qualification << "\n";
        cout << "Experience          : " << employees[id].experience << " years\n";
        cout << "Contact Number      : " << employees[id].contactNumber << "\n";
        cout << "-----------------------------------\n";
    }
    else
    {
        cout << "ERROR : ENTERED EMPLOYEE ID DOES NOT EXIST\n";
    }
}
int main()
{
    int numEmployees;
    cout << "Enter the number of employees: ";
    cin >> numEmployees;
    for (int i = 0; i < numEmployees; i++)
    {
        addEmployee();
    }
    char choice;
    int id;
    do
    {
        cout << "Enter an employee id : ";
        cin >> id;
        getEmployeeDetails(id);
        cout << "Press Y to get another employee detail, Press N to exit : ";
        cin >> choice;
    } while (choice == 'Y' || choice == 'y');
    return 0;
}