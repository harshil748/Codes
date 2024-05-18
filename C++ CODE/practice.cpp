#include <iostream>
using namespace std;
class Converter
{
private:
    double millimeters;

public:
    // Constructor
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
    double lengthInMillimeters;
    cout << "Enter length in millimeters: ";
    cin >> lengthInMillimeters;
    // Creating an object of LengthConverter class with length in millimeters
    Converter length(lengthInMillimeters);
    // Converting length to centimeters using class-to-class type conversion
    double lengthInCentimeters = length;
    cout << "Length in centimeters: " << lengthInCentimeters << " cm\n";
    // Converting length to millimeters using overloaded assignment operator
    double lengthInCentimetersInput;
    cout << "Enter length in centimeters: ";
    cin >> lengthInCentimetersInput;
    length = lengthInCentimetersInput; // Assigning length in centimeters
    double updatedLengthInMillimeters = length;
    cout << "Length in millimeters: " << updatedLengthInMillimeters * 10 << " mm\n";
    return 0;
}