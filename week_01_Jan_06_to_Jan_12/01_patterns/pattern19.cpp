#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    for (int i = 0; i < n * 2; i++)
    {
        if (i < n)
        {
            for (int j = 0; j < n - i; j++)
            {
                cout << "*";
            }
            for (int spaces = 0; spaces < i * 2; spaces++)
            {
                cout << " ";
            }
            for (int k = 0; k < n - i; k++)
            {
                cout << "*";
            }
        }
        else
        {
            for (int j = 0; j <= i - n; j++)
            {
                cout << "*";
            }
            for (int spaces = (n - 1) * 2; spaces > (i - n) * 2; spaces--)
            {
                cout << " ";
            }
            for (int k = 0; k <= i - n; k++)
            {
                cout << "*";
            }
        }

        cout << endl;
    }

    return 0;
}