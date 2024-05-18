#include <iostream>
#include <cmath>
using namespace std;
class Circle
{
public:
    double radius;
    static int totalobjects;
    Circle() : radius(1)
    {
        totalobjects++;
    }
    Circle(double r) : radius(r)
    {
        totalobjects++;
    }
    Circle(const Circle &c) : radius(c.radius)
    {
        totalobjects++;
    }
    ~Circle()//
    {
        totalobjects--;
        cout << "One object is deleted \n Total active objects: " << totalobjects << endl;
    }
    double getradius() const
    {
        return radius;
    }
    double getarea() const
    {
        return 3.14 * radius * radius;
    }
    static int gettotalobjects()
    {
        return totalobjects;
    }
};
int Circle::totalobjects = 0;
int main()
{
    Circle c1, c2(20), c3(c2);
    cout << "Circle with radius " << c1.getradius() << " has area " << c1.getarea() << endl;
    cout << "Total active objects are " << Circle::gettotalobjects() << endl;
    cout << "Circle with radius " << c2.getradius() << " has area " << c2.getarea() << endl;
    cout << "Total active objects are " << Circle::gettotalobjects() << endl;
    cout << "Circle with radius " << c3.getradius() << " has area " << c3.getradius() << endl;
    cout << "Total active objects are " << Circle::gettotalobjects() << endl;
    return 0;
}