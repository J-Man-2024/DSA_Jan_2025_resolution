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
        for (int j = startChar + n - i; j < startChar + n; j++)
        {
            cout << char(j) << " ";
        }
        cout << endl;
    }

    return 0;
}