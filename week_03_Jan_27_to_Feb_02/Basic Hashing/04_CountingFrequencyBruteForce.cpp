#include <iostream>
#include <vector>
using namespace std;

void freqCount(vector<int> &arr, int n)
{
    vector<bool> visited(n, false);
    for (int i = 0; i < n; i++)
    {
        if (visited[i] == true)
            continue;
        int count = 1;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] == arr[j])
            {
                count++;
                visited[j] = true;
            }
        }
        cout << arr[i] << " visited " << count << " times." << endl;
    }
}

int main()
{
    vector<int> arr = {10, 5, 10, 15, 10, 5};
    int n = arr.size();
    freqCount(arr, n);
    return 0;
}