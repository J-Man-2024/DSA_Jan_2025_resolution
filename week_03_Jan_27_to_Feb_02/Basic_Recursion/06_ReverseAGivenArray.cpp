#include <iostream>
using namespace std;

void reverseAnArray(int arr[], int start, int end)
{
    if (start < end)
    {
        swap(arr[start], arr[end]);
        reverseAnArray(arr, start + 1, end - 1);
    }
}
int main()
{
    int n;
    cout << "Enter the number of elements you want in an array: ";
    cin >> n;
    cout << "Enter array elements: ";
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    reverseAnArray(arr, 0, n - 1);

    cout << "Your reversed array is: " << endl;

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}