#include <iostream>
using namespace std;
int main()
{
    float experience;
    int years, months;
    cout << "Enter employee experience: ";
    cin >> experience;
    years = (int)experience;
    months = (experience - years) * 12;
    cout << "Employee experience is " << years << " years and " << months << " months" << endl;
    return 0;
}