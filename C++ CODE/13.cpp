#include <iostream>
#include <map>
#include <string>
using namespace std;
class Employee
{
public:
    int employeeID;
    string name,qualification,contactNumber;
    double experience;
    Employee(int id, string n, string q, double exp, string c)
    {
        employeeID = id;
        name = n;
        qualification = q;
        experience = exp;
        contactNumber = c;
    }
    virtual void getEmployeeData()
    {
        cout << "Employee ID: " << employeeID << endl;
        cout << "Name: " << name << endl;
        cout << "Qualification: " << qualification << endl;
        cout << "Experience: " << experience << " years\n";
        cout << "Contact Number: " << contactNumber << endl;
    }
};

class TeachingEmployee : public Employee
{
public:
    string designation, specialization;
    int payScale;
    TeachingEmployee(int id, string n, string q, double exp, string c, string des, string spec, int ps)
        : Employee(id, n, q, exp, c), designation(des), specialization(spec), payScale(ps) {}

    void getEmployeeData() override
    {
        Employee::getEmployeeData();
        cout << "Designation: " << designation << endl;
        cout << "Specialization: " << specialization << endl;
        cout << "Pay Scale: " << payScale << endl;
    }
};

class NonTeachingEmployee : public Employee
{
public:
    double salary;
    NonTeachingEmployee(int id, string n, string q, double exp, string c, double s)
        : Employee(id, n, q, exp, c), salary(s) {}

    void getEmployeeData() override
    {
        Employee::getEmployeeData();
        cout << "Salary: " << salary << endl;
    }
};
map<int, Employee *> employees;
void addEmployee()
{
    int id;
    string name, qualification, contactNumber;
    double experience;
    char type;
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
    cout << "Enter Employee Type (T - Teaching, N - Non-Teaching): ";
    cin >> type;
    if (type == 'T' || type == 't')
    {
        string designation, specialization;
        int payScale;
        cin.ignore();
        cout << "Enter Designation: ";
        getline(cin, designation);
        cout << "Enter Specialization: ";
        getline(cin, specialization);
        cout << "Enter Pay Scale: ";
        cin >> payScale;
        employees[id] = new TeachingEmployee(id, name, qualification, experience, contactNumber, designation, specialization, payScale);
    }
    else if (type == 'N' || type == 'n')
    {
        int salary;
        cout << "Enter Salary: ";
        cin >> salary;
        employees[id] = new NonTeachingEmployee(id, name, qualification, experience, contactNumber, salary);
    }
    else
    {
        cout << "Invalid Employee Type\n";
    }
}
void getEmployeeDetails(int id)
{
    if (employees.find(id) != employees.end())
    {
        employees[id]->getEmployeeData();
    }
    else
    {
        cout << "ERROR : ENTERED EMPLOYEE ID DOES NOT EXIST\n";
    }
}
double calculateAverageExperience()
{
    double totalExperience = 0;
    for (const auto &pair : employees)
    {
        totalExperience += pair.second->experience;
    }
    return totalExperience / employees.size();
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
        cout << "Enter an employee id: ";
        cin >> id;
        getEmployeeDetails(id);
        cout << "Press Y to get another employee detail, Press N to exit: ";
        cin >> choice;
    } while (choice == 'Y' || choice == 'y');
    double averageExperience = calculateAverageExperience();
    cout << "Average Experience of Employees: " << averageExperience << " years\n";
    return 0;
}