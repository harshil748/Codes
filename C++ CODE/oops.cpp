/*Develop an application that will determine whether any of several department-store
customers has exceeded the credit limit on a charge account. For each customer, the
following facts are available: (a) account number (b) balance at the beginning of the month
(c) total of all items charged by the customer this month (d) total of all credits applied to
the customer's account this month (e) allowed credit limit. The program should input all
these facts as integers, calculate the new balance (= beginning balance + charges -
credits), display the new balance and determine whether the new balance exceeds the
customer's credit limit. For those customers whose credit limit is exceeded, the program
should display the message "Credit limit exceeded".*/
#include <iostream>
using namespace std;
class Customer
{
public:
    int accountnumber;
    int beginningbalance;
    int totalcharges;
    int totalcredits;
    int creditlimit;
    void getdata()
    {
        cout << "Enter account number: ";
        cin >> accountnumber;
        cout << "Enter beginning balance: ";
        cin >> beginningbalance;
        cout << "Enter total charges: ";
        cin >> totalcharges;
        cout << "Enter credit line: ";
        cin >> creditlimit;
        cout << "Enter total credits: ";
        cin >> totalcredits;
    }
    void calculatedata()
    {
        int newbalance = beginningbalance + totalcharges - totalcredits;
        cout << "New balance is " << newbalance << endl;
        if (newbalance > creditlimit)
        {
            cout << "Credit limit exceeded" << endl;
        }
    }
};
int main()
{
    int accountnumber;
    Customer c1;
    c1.getdata();
    c1.calculatedata();
    return 0;
}