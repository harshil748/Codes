#include <iostream>
#include <map>
#include <string>
using namespace std;
int main()
{
    map<string, double> expenses;
    string item;
    double amount;
    while (true)
    {
        cout << "Enter expense name or type 'done' to quit: ";
        cin >> item;
        if (item == "done")
        {
            break;
        }
        cout << "Enter expense amount: ";
        cin >> amount;
        expenses[item] = amount;
        double total = 0;
        for (const auto &expense : expenses)
        {
            total += expense.second;
        }
        cout << "Running total: " << total << endl;
    }
    return 0;
}