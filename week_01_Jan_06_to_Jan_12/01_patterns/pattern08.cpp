#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;

    int count = n * 2 - 1;
    for (int i = 0; i < n; i++)
    {
        for (int space = 0; space < i; space++)
        {
            cout << " ";
        }
        for (int j = 0; j < count; j++)
        {
            cout << "*";
        }
        cout << endl;
        count = count - 2;
    }
    return 0;
}