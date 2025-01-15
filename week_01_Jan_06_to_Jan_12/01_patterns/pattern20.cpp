#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;

    for (int i = 0; i < n * 2 - 1; i++)
    {
        int stars = i < n ? i : (n * 2 - 2) - i;
        int spaces = (n - 1 - stars) * 2;
        for (int j = 0; j <= stars; j++)
        {
            cout << "*";
        }
        for (int space = 0; space < spaces; space++)
        {
            cout << " ";
        }
        for (int k = 0; k <= stars; k++)
        {
            cout << "*";
        }

        cout << endl;
    }
    return 0;
}