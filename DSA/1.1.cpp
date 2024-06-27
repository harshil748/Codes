#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
void printPairsDivisibleByK(const vector<int> &arr, int k)
{
    unordered_map<int, int> freq;
    for (size_t i = 0; i < arr.size(); ++i)
    {
        int remainder = arr[i] % k;
        freq[remainder]++;
    }

    for (size_t i = 0; i < arr.size(); ++i)
    {
        int remainder = arr[i] % k;
        int complement = (k - remainder) % k;

        if (remainder == 0 && freq[remainder] > 1)
        {
            cout << "(" << arr[i] << ", " << arr[i] << ")" << endl;
            freq[remainder] -= 2;
        }
        else if (remainder != 0 && freq[remainder] > 0 && freq[complement] > 0)
        {
            cout << "(" << arr[i] << ", " << k - remainder << ")" << endl;
            freq[remainder]--;
            freq[complement]--;
        }
    }
}
int main()
{
    int arr_data[] = {3, 1, 2, 6, 9, 4};
    vector<int> arr(arr_data, arr_data + sizeof(arr_data) / sizeof(arr_data[0]));
    int k = 5;
    cout << "Pairs can be formed:" << endl;
    printPairsDivisibleByK(arr, k);
    return 0;
}