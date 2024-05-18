#include <iostream>
using namespace std;
class Convert
{
public:
    double value;
    string unit;
    Convert(double value, string unit)
    {
        this->value = value;
        this->unit = unit;
    }
    Convert convertToCentimeters()
    {
        if (unit == "mm")
        {
            return Convert(value / 10.0, "cm");
        }
        else
        {
            cout << "Error: Measurement unit is not millimeters (mm)." << endl;
            return Convert(0.0, "cm");
        }
    }
    Convert convertToMillimeters()
    {
        if (unit == "cm")
        {
            return Convert(value * 10.0, "mm");
        }
        else
        {
            cout << "Error: Measurement unit is not centimeters (cm)." << endl;
            return Convert(0.0, "mm");
        }
    }
    void displayMeasurement()
    {
        cout << value << " " << unit << endl;
    }
};
int main()
{
    int choice;
    cout << "Enter 1: mm to cm converter" << endl;
    cout << "Enter 2: cm to mm converter" << endl;
    cin >> choice;
    if (choice == 1)
    {
        double mmValue;
        cout << "Enter measurement in millimeters (mm): ";
        cin >> mmValue;
        Convert mmConverter(mmValue, "mm");
        Convert cmConverter = mmConverter.convertToCentimeters();
        cout << "Measurement in centimeters (cm): ";
        cmConverter.displayMeasurement();
    }
    else if (choice == 2)
    {
        double cmValue;
        cout << "Enter measurement in centimeters (cm): ";
        cin >> cmValue;
        Convert cmConverter(cmValue, "cm");
        Convert mmConverter = cmConverter.convertToMillimeters();
        cout << "Measurement in millimeters (mm): ";
        mmConverter.displayMeasurement();
    }
    else
    {
        cout << "Invalid choice." << endl;
    }
    return 0;
}