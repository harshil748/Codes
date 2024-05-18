#include <iostream>
#include <string>
using namespace std;
class employee
{
public:
    static int number;
    string name;
    int id;
    string qulification;
    float experience;
    int no;
    static float sum;

    const void getData()
    {
        cout << "Enter Employee ID:";
        cin >> id;
        cout << "Enter Employee name:";
        cin.ignore();
        getline(cin, name);
        cout << "Enter Employee's qoulification:";
        getline(cin, qulification);
        cout << "Enter Employee's Experience:";
        cin >> experience;
        cout << "Enter Employee's Contact number:";
        cin >> no;
        sum = sum + experience;
    }
    void print(int choice)
    {
        bool f = false;
        if (choice == id)
        {
            putData();
            f = true;
        }

        else
        {
            if (!f)
            {
                cout << "ERROR : ENTERED EMPLOYEE ID DOES NOT EXIST.";
            }
        }
    }
    const void putData()
    {
        cout << "Employee name:" << name << endl;
        cout << "Qoulification:" << qulification << endl;
        cout << "Experience:" << experience << endl;
        cout << "Contact number:" << no << endl;
        cout << "Average experience:" << average() << endl;
    }
    static float average()
    {
        return sum / number;
    }
};
class teachingEmployee : public employee
{
    string designation, specialization, payScale;

public:
    void getData()
    {
        cout << "Enter Employee designation:";
        cin.ignore();
        getline(cin, designation);
        cout << "Enter Employee specialization:";
        getline(cin, specialization);
        cout << "Enter Employee pay scale:";
        getline(cin, payScale);
    }
    void putData()
    {
        cout << "Designation:" << designation << endl;
        cout << "Specialization:" << specialization << endl;
        cout << "Pay Scale:" << payScale << endl;
    }
};
class nonteachingEmployee : public employee
{
    int salary;

public:
    void getData()
    {
        cout << "Enter Employee salary:";
        cin >> salary;
    }
    void putData()
    {
        cout << "Salary:" << salary << endl;
    }
};
int employee::number = 0;
float employee::sum = 0;
int main()
{
    int n, i, choice;
    char extraChoice;

    cout << "Enter Number of Teaching Employee:";
    cin >> n;
    teachingEmployee te[n];
    for (i = 0; i < n; i++)
    {
        te[i].employee::getData();
        te[i].teachingEmployee::getData();
    }

    cout << "Enter Number of Non Teaching Employee:";
    cin >> n;
    nonteachingEmployee nte[n];
    for (i = 0; i < n; i++)
    {
        nte[i].employee::getData();
        nte[i].nonteachingEmployee::getData();
    }
    cout << endl;
    do
    {
        cout << "Enter Employee ID:";
        cin >> choice;
        for (i = 0; i < n; i++)
        {
            te[i].print(choice);
            nte[i].print(choice);
            if (te[i].id == choice)
            {
                te[i].employee::putData();
                te[i].teachingEmployee::putData();
            }
            if (nte[i].id == choice)
            {
                nte[i].employee::putData();
                nte[i].nonteachingEmployee::putData();
            }
            else
            {
                cout << "Error";
            }
        }
        cout << "Press Y to get another employee detail, Press N to exit:";
        cin >> extraChoice;
    } while (extraChoice == 'Y' || extraChoice == 'y');
    return 0;
}