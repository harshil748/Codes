#include <iostream>
using namespace std;
class areacalculator
{
public:
    float calculate(float radius)//
    {
        return 3.14 * radius * radius;
    }
    float calculate(float height, float width)
    {
        return height * width;
    }
    float calculate(float height, float width, float depth)
    {
        return 2 * (height * width + height * depth + width * depth);
    }
};
int main()
{
    areacalculator calculate;
    float radius, height, width, depth;
    cout << "Enter the radius of a circle: ";
    cin >> radius;
    cout << "The area of a circle is " << calculate.calculate(radius) << endl;
    cout << "Enter the height of a rectangle: ";
    cin >> height;
    cout << "Enter the width of a reactangle: ";
    cin >> width;
    cout << "The area of a reactangle is " << calculate.calculate(height, width) << endl;
    cout << "Enter the height of a cuboid: ";
    cin >> height;
    cout << "Enter the width of a cuboid: ";
    cin >> width;
    cout << "Enter the depth of a cuboid: ";
    cin >> depth;
    cout << "The area of a cuboid is " << calculate.calculate(height, width, depth) << endl;
    return 0;
}