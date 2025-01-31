#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// brute force
void highAndLowBrute(vector<int> &arr, int n)
{
    vector<bool> visited(n, false);
    int maxFreq = 0, minFreq = n + 1;
    int maxElement = -1, minElement = -1;

    for (int i = 0; i < n; i++)
    {
        if (visited[i])
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
        if (count > maxFreq)
        {
            maxFreq = count;
            maxElement = arr[i];
        }

        if (count < minFreq)
        {
            minFreq = count;
            minElement = arr[i];
        }
    }

    cout << "Element with highest frequency: " << maxElement << " (count: " << maxFreq << ")" << endl;
    cout << "Element with Lowest frequency: " << minElement << " (count: " << minFreq << ")" << endl;
}

// Optimized
void highAndLowOptimized(vector<int> &arr)
{
    unordered_map<int, int> umap;

    for (int num : arr)
    {
        umap[num]++;
    }
    int maxFreq = 0, minFreq = arr.size() + 1;
    int maxElement = -1, minElement = -1;
    for (const auto &it : umap)
    {

        if (it.second > maxFreq)
        {
            maxFreq = it.second;
            maxElement = it.first;
        }
        if (it.second < minFreq)
        {
            minFreq = it.second;
            minElement = it.first;
        }
    }
    cout << "Element with highest frequency: " << maxElement << " (count: " << maxFreq << ")" << endl;
    cout << "Element with lowest frequency: " << minElement << " (count: " << minFreq << ")" << endl;
}
int main()
{
    vector<int> arr = {10, 5, 10, 15, 10, 5};
    highAndLowOptimized(arr);
    return 0;
}