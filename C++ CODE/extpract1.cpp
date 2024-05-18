#include <iostream>
using namespace std;
class HEIGHT
{
public:
    float cm;

public:
    HEIGHT()
    {
        cm = 0.0;
    }
    HEIGHT(float value)
    {
        cm = value;
    }
    void input()
    {
        cout << "Enter height in centimeters: ";
        cin >> cm;
    }
    void display()
    {
        cout << "Height: " << cm << " centimeters" << endl;
    }
    HEIGHT operator+(const HEIGHT &h2)
    {
        HEIGHT result;
        result.cm = this->cm + h2.cm;
        return result;
    }
    friend HEIGHT operator+(float value, const HEIGHT &h2)
    {
        HEIGHT result;
        result.cm = value + h2.cm;
        return result;
    }
};
int main()
{
    HEIGHT H1, H2, H3;
    cout << "Enter height for H1" << endl;
    H1.input();
    cout << "Enter height for H2" << endl;
    H2.input();
    cout << "Height for H1: ";
    H1.display();
    cout << "Height for H2: ";
    H2.display();
    H3 = 2.0 + H2;
    cout << "After adding 2.0 to H2, the result is:  " << endl;
    H3.display();
    return 0;
}