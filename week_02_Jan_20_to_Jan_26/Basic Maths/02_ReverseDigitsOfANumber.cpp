#include <iostream>
using namespace std;

int reverseNumber(int n)
{
    int revNum = 0;
    while (n > 0)
    {
        int lastDigit = n % 10;
        revNum = revNum * 10 + lastDigit;

        n = n / 10;
    }
    return revNum;
}

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    int ans = reverseNumber(n);
    cout << ans;
    return 0;
}