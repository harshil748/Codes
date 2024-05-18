#include <iostream>
using namespace std;
class Complex
{
private:
    int real;
    int imag;

public:
    Complex(int r = 0, int i = 0) : real(r), imag(i) {}
    Complex operator+(const Complex &other) const
    {
        return Complex(real + other.real, imag + other.imag);
    }
    Complex operator-(const Complex &other) const
    {
        return Complex(real - other.real, imag - other.imag);
    }
    Complex operator*(const Complex &other) const
    {
        return Complex(real * other.real - imag * other.imag, real * other.imag + imag * other.real);
    }
    Complex operator/(const Complex &other) const
    {
        int denominator = other.real * other.real + other.imag * other.imag;
        return Complex((real * other.real + imag * other.imag) / denominator, (imag * other.real - real * other.imag) / denominator);
    }
    Complex operator!() const
    {
        return Complex(-real, -imag);
    }
    friend ostream &operator<<(ostream &, const Complex &);
};
ostream &operator<<(ostream &os, const Complex &c)
{
    os << c.real << " + " << c.imag << "i";
    return os;
}
int main()
{
    cout << "Enter real part: ";
    int real, real1;
    cin >> real;
    cout << "Enter real part: ";
    cin >> real1;
    cout << "Enter imaginary part: ";
    int imag, imag1;
    cin >> imag;
    cout << "Enter imaginary part: ";
    cin >> imag1;
    Complex c1(real, imag);
    Complex c2(real1, imag1);
    Complex c3(c1);
    do
    {
        cout << "Choose operation:\n"
             << "( + ) Addition\n"
             << "( - ) Subtraction\n"
             << "( * ) Multiplication\n"
             << "( / ) Division\n"
             << "( ! ) Negation\n";
        char op;
        cin >> op;
        Complex result;
        switch (op)
        {
        case '+':
            result = c1 + c2;
            break;
        case '-':
            result = c1 - c2;
            break;
        case '*':
            result = c1 * c2;
            break;
        case '/':
            result = c1 / c2;
            break;
        case '!':
            result = !c3;
            break;
        default:
            cout << "Invalid operation!\n";
            return 1;
        }
        cout << "Result: " << result << endl;
        cout << "Do you want to continue? (y/n): ";
        char choice;
        cin >> choice;
        if (choice == 'n' || choice == 'N')
        {
            break;
        }
    } while (true);
    return 0;
}