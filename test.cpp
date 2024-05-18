#include <iostream>
#include <vector>
#include <string>
using namespace std;
struct Expense
{
    string category;
    double amount;
};
void addExpense(std::vector<Expense> &expenses)
{
    Expense expense;
    cout << "Enter expense category: ";
    cin >> expense.category;
    cout << "Enter expense amount: ";
    cin >> expense.amount;
    expenses.push_back(expense);
}
void displayExpenses(const std::vector<Expense> &expenses)
{
    cout << "Expense List:\n";
    for (const auto &expense : expenses)
    {
        cout << "Category: " << expense.category << ", Amount: $" << expense.amount << "\n";
    }
}
int main()
{
    vector<Expense> expenses;
    char choice;
    do
    {
        cout << "1. Add Expense\n";
        cout << "2. Display Expenses\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case '1':
            addExpense(expenses);
            break;
        case '2':
            displayExpenses(expenses);
            break;
        case '3':
            cout << "Exiting...\n";
            break;
        default:
            cout << "Invalid choice. Please try again.\n";
            break;
        }
        cout << "\n";
    } while (choice != '3');
    return 0;
}