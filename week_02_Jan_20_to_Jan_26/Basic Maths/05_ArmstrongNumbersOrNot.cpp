#include <iostream>
#include <math.h>
using namespace std;

bool armStrong(int n)
{
    int cpy = n;
    int len = (int)log10(n) + 1;
    int sum = 0;
    for (int i = 1; i <= len; i++)
    {
        int ld = n % 10;
        sum += pow(ld, len);
        n = n / 10;
    }

    if (sum == cpy)
        return 1;

    return 0;
}
int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    int ans = armStrong(n);
    if (ans)
    {
        cout << "Yes! " << n << " is an armstrong number." << endl;
    }
    else
    {
        cout << "No! " << n << " is not an armstrong number." << endl;
    }

    return 0;
}