#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter length of the array: ";
    cin >> n;
    int arr[n];
    cout << "Enter the array elements: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int hash[13] = {0};
    for (int i = 0; i < n; i++)
    {
        hash[arr[i]]++;
    }

    int q;
    cout << "How many queries do you want to check?" << endl;
    cin >> q;

    while (q--)
    {
        int num;
        cout << "Enter the element you want to check: ";
        cin >> num;
        cout << num << " Appears, ";
        cout << hash[num] << " times." << endl;
    }
    return 0;
}