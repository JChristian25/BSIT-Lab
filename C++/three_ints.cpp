#include <iostream>

int main ()
{
    int a, b, c, sum;
    std::cout << "Enter three integers: ";
    std::cin >> a;
    std::cin >> b;
    std::cin >> c;
    sum = 2 * (a + b + c);
    sum += c;
    std::cout << "Twice the sum of your integers plus " << c << " is "
    << sum << " - bye!" << std::endl;
}