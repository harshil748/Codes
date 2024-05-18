/*Create a C++ code for millimeter and centimeter measurement converter.*/
#include <iostream>
using namespace std;
class Converter
{
public:
    double millimeters;
    Converter(double mm) : millimeters(mm) {}
    // Conversion to centimeters
    operator double() const
    {
        return millimeters / 10.0;
    }
    // Conversion to millimeters
    Converter operator=(double cm)
    {
        millimeters = cm * 10.0;
        return *this;
    }
};
int main()
{
    double InMillimeters;
    cout << "Enter length in millimeters: ";
    cin >> InMillimeters;
    // Creating an object of LengthConverter class with length in millimeters
    Converter length(InMillimeters);
    // Converting length to centimeters using class-to-class type conversion
    double InCentimeters = length;
    cout << "Length in centimeters: " << InCentimeters << " cm\n";
    // Converting length to millimeters using overloaded assignment operator
    double InCentimetersInput;
    cout << "Enter length in centimeters: ";
    cin >> InCentimetersInput;
    length = InCentimetersInput; // Assigning length in centimeters
    double LengthInMillimeters = length;
    cout << "Length in millimeters: " << LengthInMillimeters * 10 << " mm\n";
    return 0;
}