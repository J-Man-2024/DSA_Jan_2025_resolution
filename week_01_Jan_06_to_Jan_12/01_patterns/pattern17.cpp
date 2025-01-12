#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;

    int startChar = 'A';

    for (int i = 1; i <= n; i++)
    {
        for (int spaces = 1; spaces <= n - i; spaces++)
        {
            cout << " ";
        }
        for (int j = startChar; j < startChar + i; j++)
        {
            cout << char(j);
        }
        for (int k = startChar + i - 2; k >= startChar; k--)
        {
            cout << char(k);
        }
        cout << endl;
    }
    return 0;
}