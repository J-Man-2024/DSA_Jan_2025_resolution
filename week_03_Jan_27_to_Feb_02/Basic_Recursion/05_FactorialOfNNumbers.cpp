#include <iostream>
using namespace std;

int factorialOfN(int n)
{
    if (n == 0)
        return 1;

    return factorialOfN(n - 1) * n;
}

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    int ans = factorialOfN(n);
    cout << "The factorial of " << n << " is: " << ans << "." << endl;
    return 0;
}