#include <iostream>
using namespace std;
class Product
{
private:
    int product_id;
    string product_name;
    string product_manufacturer;
    float product_price;
public:
    Product(int id, string name, string manufacturer, float price)
{
    product_id = id;
    product_name = name;
    product_manufacturer = manufacturer;
    product_price = price;
}

    int get_product_id() { return product_id; }
    string get_product_name() { return product_name; }
    string get_product_manufacturer() { return product_manufacturer; }
    float get_product_price() { return product_price; }
    void set_product_id(int id) { product_id = id; }
    void set_product_name(string name) { product_name = name; }
    void set_product_manufacturer(string manufacturer) { product_manufacturer = manufacturer; }
    void set_product_price(float price) { product_price = price; }
    virtual void putdata() = 0;
};
class Smartwatch : public Product
{
private:
    float dial_size;

public:
    Smartwatch(int id, string name, string manufacturer, float price, float size) : Product(id, name, manufacturer, price), dial_size(size) {}
    float get_dial_size() { return dial_size; }
    void set_dial_size(float size) { dial_size = size; }
    void putdata()
    {
        cout << "------------------------------------------------"<< endl;
        cout << get_product_id() << " : " << get_product_name() << " : "<< get_product_manufacturer() << " : " << get_product_price() << " : " << get_dial_size() << endl;
        cout << "------------------------------------------------"<< endl;
    }
};
class BedSheet : public Product
{
private:
    float width;
    float height;

public:
    BedSheet(int id, string name, string manufacturer, float price, float w, float h) : Product(id, name, manufacturer, price), width(w), height(h) {}
    float get_width() { return width; }
    void set_width(float w) { width = w; }
    float get_height() { return height; }
    void set_height(float h) { height = h; }
    void putdata()
    {
        cout << "-------------------------------------------------------"<< endl;
        cout << get_product_id() << " : " << get_product_name() << " : "<< get_product_manufacturer() << " : " << get_product_price() << " : " << get_width() << " : " << get_height() << endl;
        cout << "-------------------------------------------------------"<< endl;
    }
};
int main()
{
    int choice;
    while (true)
    {
        cout << "Enter 1: Smartwatch menu" << endl;
        cout << "Enter 2: Bed sheet menu" << endl;
        cout << "Enter 3: Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        if (choice == 1)
        {
            int product_id;
            string product_name;
            string product_manufacturer;
            float product_price;
            float dial_size;
            cout << "Enter product id: ";
            cin >> product_id;
            cout << "Enter product name: ";
            cin.ignore();
            getline(cin, product_name);
            cout << "Enter product manufacturer: ";
            cin >> product_manufacturer;
            cout << "Enter product price: ";
            cin >> product_price;
            cout << "Enter dial size: ";
            cin >> dial_size;
            Smartwatch smartwatch(product_id, product_name, product_manufacturer, product_price, dial_size);
            smartwatch.putdata();
        }
        else if (choice == 2)
        {
            int product_id;
            string product_name;
            string product_manufacturer;
            float product_price;
            float width;
            float height;
            cout << "Enter product id: ";
            cin >> product_id;
            cout << "Enter product name: ";
            cin.ignore();
            getline(cin, product_name);
            cout << "Enter product manufacturer: ";
            cin >> product_manufacturer;
            cout << "Enter product price: ";
            cin >> product_price;
            cout << "Enter width: ";
            cin >> width;
            cout << "Enter height: ";
            cin >> height;
            BedSheet bedsheet(product_id, product_name, product_manufacturer, product_price, width, height);
            bedsheet.putdata();
        }
        else 
        {
            break;
        }
    }
    return 0;
}