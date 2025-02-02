#include <iostream>
#include <vector>
using namespace std;

void sorted(vector<int> &arr, int start, int mid, int end)
{
    int leftHalf = start;
    int rightHalf = mid + 1;
    vector<int> sortedArr;

    while (leftHalf <= mid && rightHalf <= end)
    {
        if (arr[leftHalf] <= arr[rightHalf])
        {
            sortedArr.push_back(arr[leftHalf]);
            leftHalf++;
        }
        else
        {
            sortedArr.push_back(arr[rightHalf]);
            rightHalf++;
        }
    }

    while (leftHalf <= mid)
    {
        sortedArr.push_back(arr[leftHalf]);
        leftHalf++;
    }
    while (rightHalf <= end)
    {
        sortedArr.push_back(arr[rightHalf]);
        rightHalf++;
    }

    for (int i = 0; i < sortedArr.size(); i++)
    {
        arr[start + i] = sortedArr[i];
    }
}

void mergeSort(vector<int> &arr, int start, int end)
{
    if (start < end)
    {
        int mid = start + (end - start) / 2;
        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);
        sorted(arr, start, mid, end);
    }
}
int main()
{
    vector<int> arr = {4, 2, 1, 6, 7};
    int n = arr.size();
    mergeSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}