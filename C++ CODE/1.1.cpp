#include <iostream>
using namespace std;
int main()
{
    int num1, num2;
    char op;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;
    cout << "Enter an operation (+, -, *, /): ";
    cin >> op;
    int result;
    switch (op)
    {
    case '+':
        result = num1 + num2;
        break;
    case '-':
        result = num1 - num2;
        break;
    case '*':
        result = num1 * num2;
        break;
    case '/':
        if (num2 == 0)
        {
            cout << "Error: division by zero" << endl;
            return 1;
        }
        result = num1 / num2;
        break;
    default:
        cout << "Error: invalid operation" << endl;
        return 1;
    }
    cout << "Result: " << result << endl;
    return 0;
}
