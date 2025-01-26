#include <iostream>
using namespace std;

bool primeOrNotBruteForce(int n)
{
    int count = 0;
    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            count++;
        }
    }
    if (count == 2)
    {
        return true;
    }

    return false;
}

bool primeOrNotOptimized(int n)
{
    int count = 0;
    for (int i = 1; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            count++;
            if (n / i != i)
            {
                count++;
            }
        }
    }
    if (count == 2)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;

    if (primeOrNotOptimized(n))
    {
        cout << "Yes! " << n << " is a prime number.";
    }
    else
    {
        cout << "No! " << n << " is not a prime number.";
    }
    return 0;
}