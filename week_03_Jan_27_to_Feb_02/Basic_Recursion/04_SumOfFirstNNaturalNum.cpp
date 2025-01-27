#include <iostream>
using namespace std;

int sumOfFirstNNum(int n)
{
    if (n == 1)
        return 1;

    return sumOfFirstNNum(n - 1) + n;
}

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    int ans = sumOfFirstNNum(n);
    cout << "The sum of " << n << " is: " << ans << "." << endl;
    return 0;
}