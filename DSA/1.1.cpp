#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
void printPairsDivisibleByK(const vector<int> &arr, int k)
{
    unordered_map<int, int> freq;
    for (int num : arr)
    {
        int remainder = num % k;
        freq[remainder]++;
    }
    for (int num : arr)
    {
        int remainder = num % k;
        int complement = (k - remainder) % k;
        if (freq[complement] > 0)
        {
            freq[complement]--;
            cout << "(" << num << ", " << complement << ")" << endl;
        }
    }
}
int main()
{
    vector<int> arr = {3, 1, 2, 6, 9, 4};
    int k = 5;
    cout << "Pairs can be formed:" << endl;
    printPairsDivisibleByK(arr, k);
    return 0;
}