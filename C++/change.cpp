#include <iostream>
using namespace std;

int main ()
{
    int price, change, dimes, pennies;

    cout << "Enter price (0:100): ";
    cin >> price;
    change = 100 - price;
    dimes = change / 10;
    pennies = change % 10;
    cout << "\n\nThe change is: "
        << dimes << " dimes ";
    cout << pennies << " pennies." << endl;
}