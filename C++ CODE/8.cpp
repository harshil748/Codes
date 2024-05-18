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
/*
#include <iostream>
#include <map>
#include <string>
using namespace std;
class Employee
{
public:
    int empID;
    string empName;
    string qualification;
    double experience;
    string contact;
    void getempdata();
    void putempdata();
    void searchemp();
    virtual double avgexp() = 0;
};
class TeachingEmployee : public Employee
{
public:
    string designation;
    string specialization;
    string payScale;
    void searchtemp();
    void gettempdata();
    void puttempydata();
    double avgexp();
};
class NonTeachingEmployee : public Employee
{
public:
    int salary;
    void searchntemp();
    void getntempdata();
    void putntempdata();
    double avgexp();
};
map<int, TeachingEmployee> teachingEmployees;
map<int, NonTeachingEmployee> nonTeachingEmployees;
void Employee::getempdata()
{
    cout << "Enter Employee ID: ";
    cin >> empID;
    cin.ignore();
    cout << "Enter Employee Name: ";
    getline(cin, empName);
    cout << "Enter Qualification: ";
    getline(cin, qualification);
    cout << "Enter Experience: ";
    cin >> experience;
    cout << "Enter Contact Number: ";
    cin >> contact;
}
void Employee::putempdata()
{
    cout << "Employee ID: " << empID << endl;
    cout << "Employee Name: " << empName << endl;
    cout << "Qualification: " << qualification << endl;
    cout << "Experience: " << experience << " years" << endl;
    cout << "Contact Number: " << contact << endl;
}
void Employee::searchemp()
{
    int id;
    cout << "Enter Employee ID to search: ";
    cin >> id;
    if (teachingEmployees.find(id) != teachingEmployees.end())
    {
        teachingEmployees[id].putempdata();
    }
    else if (nonTeachingEmployees.find(id) != nonTeachingEmployees.end())
    {
        nonTeachingEmployees[id].putempdata();
    }
    else
    {
        cout << "Employee not found." << endl;
    }
}
void TeachingEmployee::searchtemp()
{
    int id;
    cout << "Enter Teaching Employee ID to search: ";
    cin >> id;
    if (teachingEmployees.find(id) != teachingEmployees.end())
    {
        teachingEmployees[id].putempdata();
    }
    else
    {
        cout << "Teaching Employee not found." << endl;
    }
}
void TeachingEmployee::gettempdata()
{
    Employee::getempdata();
    cin.ignore();
    cout << "Enter Designation: ";
    getline(cin, designation);
    cout << "Enter Specialization: ";
    getline(cin, specialization);
    cout << "Enter Pay Scale: ";
    getline(cin, payScale);
}
void TeachingEmployee::puttempydata()
{
    Employee::putempdata();
    cout << "Designation    : " << designation << endl;
    cout << "Specialization: " << specialization << endl;
    cout << "Pay Scale: " << payScale << endl;
}
double TeachingEmployee::avgexp()
{
    double totalExperience = 0;
    for (const auto &pair : teachingEmployees)
    {
        totalExperience += pair.second.experience;
    }
    return totalExperience / teachingEmployees.size();
}
void NonTeachingEmployee::searchntemp()
{
    int id;
    cout << "Enter Non-Teaching Employee ID to search: ";
    cin >> id;
    if (nonTeachingEmployees.find(id) != nonTeachingEmployees.end())
    {
        nonTeachingEmployees[id].putempdata();
    }
    else
    {
        cout << "Non-Teaching Employee not found." << endl;
    }
}
void NonTeachingEmployee::getntempdata()
{
    Employee::getempdata();
    cout << "Enter Salary: ";
    cin >> salary;
}
void NonTeachingEmployee::putntempdata()
{
    Employee::putempdata();
    cout << "Salary: " << salary << endl;
}
double NonTeachingEmployee::avgexp()
{
    double totalExperience = 0;
    for (const auto &pair : nonTeachingEmployees)
    {
        totalExperience += pair.second.experience;
    }
    return totalExperience / nonTeachingEmployees.size();
}
int main()
{
    int numTeachingEmployees, numNonTeachingEmployees;
    cout << "Enter the number of teaching employees: ";
    cin >> numTeachingEmployees;
    for (int i = 0; i < numTeachingEmployees; i++)
    {
        TeachingEmployee newTeachingEmployee;
        cout << "Enter details for Teaching Employee #" << i + 1 << endl;
        newTeachingEmployee.gettempdata();
        teachingEmployees[newTeachingEmployee.empID] = newTeachingEmployee;
    }
    cout << "Enter the number of non-teaching employees: ";
    cin >> numNonTeachingEmployees;
    for (int i = 0; i < numNonTeachingEmployees; i++)
    {
        NonTeachingEmployee newNonTeachingEmployee;
        cout << "Enter details for Non-Teaching Employee #" << i + 1 << endl;
        newNonTeachingEmployee.getntempdata();
        nonTeachingEmployees[newNonTeachingEmployee.empID] = newNonTeachingEmployee;
    }
    char choice;
    do
    {
        cout << "Enter T to search for a teaching employee, N to search for a non-teaching employee, or X to exit: ";
        cin >> choice;
        switch (choice)
        {
        case 'T':
        case 't':
            TeachingEmployee().searchtemp();
            break;
        case 'N':
        case 'n':
            NonTeachingEmployee().searchntemp();
            break;
        case 'X':
        case 'x':
            break;
        default:
            cout << "Invalid choice. Please enter T, N, or X." << endl;
        }
    } while (choice != 'X' && choice != 'x');
    double teachingAverageExperience = TeachingEmployee().avgexp();
    double nonTeachingAverageExperience = NonTeachingEmployee().avgexp();
    cout << "Average Experience of Teaching Employees: " << teachingAverageExperience << " years" << endl;
    cout << "Average Experience of Non-Teaching Employees: " << nonTeachingAverageExperience << " years" << endl;
    cout << "Average Experience of All Employees: " << (teachingAverageExperience + nonTeachingAverageExperience) / 2 << " years" << endl;
    return 0;
}
*/