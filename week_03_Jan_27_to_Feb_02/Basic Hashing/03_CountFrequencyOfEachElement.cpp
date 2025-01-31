#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

void freqCnt(const vector<int> &arr)
{
    unordered_map<int, int> umap;
    for (int num : arr)
    {
        umap[num]++;
    }

    for (const auto &it : umap)
    {
        cout << it.first << " Appears, " << it.second << " times." << endl;
    }
}

int main()
{
    vector<int> arr = {10, 5, 10, 15, 10, 5};
    freqCnt(arr);

    return 0;
}