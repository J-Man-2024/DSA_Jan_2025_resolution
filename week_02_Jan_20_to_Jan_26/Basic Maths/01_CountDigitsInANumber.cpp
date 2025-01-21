#include <iostream>
#include <math.h>
using namespace std;

// Brute force method
int countDigitsBruteForce(int n)
{
    int count = 0;

    while (n > 0)
    {
        count++;
        n = n / 10;
    }
    return count;
}

// Optimal method
int countDigitsOptimal(int n)
{
    int count = (int)log10(n) + 1;
    return count;
}
int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    int ans = countDigitsOptimal(n);
    cout << "There are " << ans << " number of digits in " << n << ".";
    return 0;
}