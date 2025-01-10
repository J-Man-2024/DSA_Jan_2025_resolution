#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j;
        }
        for (int spaces = 0; spaces < 2 * (n - i); spaces++)
        {
            cout << " ";
        }

        for (int k = i; k >= 1; k--)
        {
            cout << k;
        }
        cout << endl;
    }
    return 0;
}