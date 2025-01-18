#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    int start = n * 2 - 1;

    for (int i = 0; i < start; i++)
    {
        for (int j = 0; j < start; j++)
        {
            int layer = min(min(i, j), min(start - 1 - i, start - 1 - j));
            int value = n - layer;
            cout << value << " ";
        }
        cout << endl;
    }

    return 0;
}