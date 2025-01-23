#include <iostream>
using namespace std;
bool palindromeOrNot(int n)
{
    int numCpy = n;
    int revNum = 0;
    while (n > 0)
    {
        int lastDigit = n % 10;
        revNum = revNum * 10 + lastDigit;
        n = n / 10;
    }
    if (numCpy == revNum)
    {
        return true;
    }

    return false;
}
int main()
{
    int n = 131;
    int ans = palindromeOrNot(n);

    if (ans == 1)
    {
        cout << "Yes! The number " << n << " is a palindrome." << endl;
    }
    else
    {
        cout << "No! The number " << n << " is not a palindrome." << endl;
    }

    return 0;
}