#include <iostream>
#include <string>
using namespace std;
const int MAX_TRAINS = 10;
struct Train
{
    int number;
    string start_station;
    string end_station;
    int coaches;
};
int main()
{
    Train trains[MAX_TRAINS];
    int train_count = 0;
    while (true)
    {
        Train new_train;
        cout << "Enter train number: ";
        cin >> new_train.number;
        cout << "Enter start station: ";
        cin >> new_train.start_station;
        cout << "Enter end station: ";
        cin >> new_train.end_station;
        cout << "Enter number of coaches: ";
        cin >> new_train.coaches;
        trains[train_count++] = new_train;
        cout << "\nTrain listing board:\n";
        for (int i = 0; i < train_count; i++)
        {
            cout << "Number: " << trains[i].number << ", Start station: " << trains[i].start_station << ", End station: " << trains[i].end_station << ", Coaches: " << trains[i].coaches << '\n';
        }
    }
    return 0;
}