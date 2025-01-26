#include <iostream>
using namespace std;

// Brute force method
void divisorsOfANumBruteForce(int n)
{
    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            cout << i << " ";
        }
    }
    cout << endl;
}

// Optimal approach
void divisorsOfANumOptimized(int n)
{
    for (int i = 1; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            cout << i << " ";
            if (i != n / i)
            {
                cout << n / i << " ";
            }
        }
    }
    cout << endl;
}
int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    divisorsOfANumBruteForce(n);
    return 0;
}