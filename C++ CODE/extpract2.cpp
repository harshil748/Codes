#include <iostream>
using namespace std;
class Shape
{
public:
    float height;
    float width;
    Shape(float h = 0.0, float w = 0.0) : height(h), width(w) {}
    virtual float getArea() = 0;
    void putArea()
    {
        cout << "Area: " << getArea() << endl;
    }
    virtual void inputDimensions()
    {
        cout << "Enter height: ";
        cin >> height;
        cout << "Enter width: ";
        cin >> width;
    }
};
class Rectangle : public Shape
{
public:
    Rectangle() {}
    void inputDimensions() override
    {
        Shape::inputDimensions();
    }
    float getArea() override
    {
        return height * width;
    }
};
class Triangle : public Shape
{
public:
    Triangle() {}
    void inputDimensions() override
    {
        Shape::inputDimensions();
    }
    float getArea() override
    {
        return 0.5 * height * width;
    }
};
int main()
{
    Rectangle rect;
    cout << "Enter dimensions for Rectangle:" << endl;
    rect.inputDimensions();
    cout << "Rectangle:" << endl;
    rect.putArea();
    Triangle tri;
    cout << "Enter dimensions for Triangle:" << endl;
    tri.inputDimensions();
    cout << "Triangle:" << endl;
    tri.putArea();
    return 0;
}