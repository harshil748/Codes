#include <iostream>
#include <string>
using namespace std;
struct Car
{
    string model_name;
    string fuel_type;
    float showroom_price;
    float mileage;
    string transmission;
    float tank_capacity;
    int seating;
    string airbags;
};
void feedCarDetails(Car cars[], int num_cars)
{
    for (int i = 0; i < num_cars; ++i)
    {
        cout << "Enter details for car " << i + 1 << ":\n";
        cout << "Model name: ";
        cin.ignore();
        getline(cin, cars[i].model_name);
        cout << "Fuel type (petrol/diesel/cng/electric):";
        cin >> cars[i].fuel_type;
        cout << "Showroom price: ";
        cin >> cars[i].showroom_price;
        cout << "Mileage: ";
        cin >> cars[i].mileage;
        cout << "Transmission (Manual/AMT): ";
        cin >> cars[i].transmission;
        cout << "Tank capacity: ";
        cin >> cars[i].tank_capacity;
        cout << "Seating: ";
        cin >> cars[i].seating;
        cout << "Airbags(Yes/No): ";
        cin >> cars[i].airbags;
    }
}
void retrieveCarData(const Car cars[], int num_cars, int option, const string &search)
{
    switch (option)
    {
    case 1:
        for (int i = 0; i < num_cars; ++i)
        {
            if (cars[i].model_name == search)
            {
                cout << " Fuel type: " << cars[i].fuel_type;
                cout << " Showroom Price: Rs." << cars[i].showroom_price << " Lakhs ";
                cout << " Mileage: " << cars[i].mileage << " Km/L ";
                cout << " Transmission: " << cars[i].transmission;
                cout << " Tank Capacity: " << cars[i].tank_capacity << " Liters ";
                cout << " Seating: " << cars[i].seating;
                cout << " Airbags: " << cars[i].airbags;
                cout << endl;
            }
        }
        break;
    case 2:
        for (int i = 0; i < num_cars; ++i)
        {
            if (cars[i].fuel_type == search)
            {
                cout << " Model Name: " << cars[i].model_name;
                cout << " Showroom Price: " << cars[i].showroom_price << " Lakhs ";
                cout << " Mileage: " << cars[i].mileage << " Km/L ";
                cout << " Transmission: " << cars[i].transmission;
                cout << " Tank Capacity: " << cars[i].tank_capacity << " Liters ";
                cout << " Seating: " << cars[i].seating;
                cout << " Airbags: " << cars[i].airbags;
                cout << endl;
            }
        }
        break;
    case 3:
        float min_price, max_price;
        cout << "Enter the minimum price: ";
        cin >> min_price;
        for (int i = 0; i < num_cars; ++i)
        {
            if (cars[i].showroom_price >= min_price && cars[i].showroom_price <= max_price)
            {
                cout << " Model Name: " << cars[i].model_name;
                cout << " Fuel Type: " << cars[i].fuel_type;
                cout << " Mileage: " << cars[i].mileage << " Km/L ";
                cout << " Transmission: " << cars[i].transmission;
                cout << " Tank Capacity: " << cars[i].tank_capacity << " Liters ";
                cout << " Seating: " << cars[i].seating;
                cout << " Airbags: " << cars[i].airbags;
                cout << endl;
            }
        }
        break;
    default:
        cout << "Invalid Option" << endl;
    }
}
int main()
{
    const int MAX_CARS = 100;
    Car cars[MAX_CARS];
    int num_cars;
    cout << "Welcome To TATA Motors\n";
    cout << "Enter the number of cars: ";
    cin >> num_cars;
    feedCarDetails(cars, num_cars);
    int option;
    cout << "Get the car details as per your preference\n";
    cout << "(1)Model Name (2)Fuel Type (3)Price Range\n";
    cout << "Enter your option: ";
    cin >> option;
    string search_key;
    if (option == 1 || option == 2)
    {
        cout << "Enter the search key: ";
        cin >> search_key;
    }
    retrieveCarData(cars, num_cars, option, search_key);
    return 0;
}