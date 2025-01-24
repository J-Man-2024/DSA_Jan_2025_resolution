#include <iostream>
using namespace std;

// Brute force method
int gcdOfTwoNumbersBruteForce(int n1, int n2)
{
    int gcd = 1;
    for (int i = 1; i <= min(n1, n2); i++)
    {
        if (n1 % i == 0 && n2 % i == 0)
            gcd = i;
    }
    return gcd;
}

// Optimal method using Euclidean formula
int gcdOfTwoNumbersOptimal(int n1, int n2)
{
    while (n1 > 0 && n2 > 0)
    {
        if (n1 > n2)
        {
            n1 = n1 % n2;
        }
        else
        {
            n2 = n2 % n1;
        }
    }

    if (n1 == 0)
        return n2;

    return n1;
}
int main()
{
    int n1, n2;
    cout << "Enter two numbers followed by space: ";
    cin >> n1 >> n2;
    int ans = gcdOfTwoNumbersOptimal(n1, n2);
    cout << "The GCD of " << n1 << " & " << n2 << " is " << ans << ".";
    return 0;
}