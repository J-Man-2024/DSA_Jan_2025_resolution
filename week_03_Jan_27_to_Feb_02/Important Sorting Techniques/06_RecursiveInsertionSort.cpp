#include <iostream>
using namespace std;

void insert(int arr[], int n)
{
    // Base case: Stop if we are at the start or in correct position
    if (n <= 0 || arr[n] >= arr[n - 1])
        return;

    // Shifting larger element right
    swap(arr[n], arr[n - 1]);

    // Continue shifting left
    insert(arr, n - 1);
}

void insertionSort(int arr[], int n)
{
    // Base case: A single element is always sorted
    if (n <= 1)
        return;

    // Recursively sort first n-1 elements
    insertionSort(arr, n - 1);
    // Insert the last element into it's correct position
    insert(arr, n - 1);
}

int main()
{
    int arr[] = {13, 46, 24, 52, 20, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    insertionSort(arr, n);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}