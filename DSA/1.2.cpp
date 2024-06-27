#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int main()
{
    string input;
    cout << "Enter a sentence: ";
    getline(std::cin, input);
    istringstream iss(input);
    string word;
    string longestWord;
    int maxLength = 0;
    while (iss >> word)
    {
        if (word.length() > maxLength)
        {
            maxLength = word.length();
            longestWord = word;
        }
    }
    cout << "Longest word's length = " << maxLength << endl;
    return 0;
}