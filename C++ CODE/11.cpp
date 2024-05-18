#include <iostream>
using namespace std;
int main()
{
  int years, months;
  cout << "Enter employee experience in years and months\n";
  cout << "Years: ";
  cin >> years;
  cout << "Months: ";
  cin >> months;
  float experience = years + (float)months / 12.0;
  cout << "Employee experience is: " << experience << endl;
  return 0;
}