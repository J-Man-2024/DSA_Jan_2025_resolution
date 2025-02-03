#include <iostream>
using namespace std;

void swapping(int arr[], int i, int n)
{
    if (i == n - 1)
        return;

    if (arr[i] > arr[i + 1])
    {
        swap(arr[i], arr[i + 1]);
    }

    swapping(arr, i + 1, n);
}
void bubbleSort(int arr[], int n)
{
    if (n == 1)
        return;

    swapping(arr, 0, n);

    bubbleSort(arr, n - 1);
}
int main()
{
    int arr[] = {13, 46, 24, 52, 20, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, n);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}