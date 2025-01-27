#include <iostream>
using namespace std;

void printName(string name, int n)
{
    if (n == 0)
        return;
    printName(name, n - 1);
    cout << name << endl;
}

int main()
{
    string name;
    int n;
    cout << "Enter a name: ";
    cin >> name;
    cout << "Enter how many times you want to print: ";
    cin >> n;
    printName(name, n);
    return 0;
}