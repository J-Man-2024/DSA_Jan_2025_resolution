#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    int count = n * 2 - 1;
    for (int i = 0; i < count; i++)
    {
        int stars = (i < n) ? i + 1 : count - i;

        for (int j = 0; j < stars; j++)
        {
            cout << "*";
        }

        cout << endl;
    }
    return 0;
}