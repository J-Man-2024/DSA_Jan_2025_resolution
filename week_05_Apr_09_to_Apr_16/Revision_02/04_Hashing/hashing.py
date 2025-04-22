from collections import Counter
from collections import defaultdict


def freq_count_brute(arr):
    n = len(arr)
    visited = [False] * n
    for i in range(n):
        if visited[i] == True:
            continue
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
                visited[j] = True
        print(f"{arr[i]} appears : {count} times.")
# It takes O(n^2) time and O(1) extra space
def freq_count_better(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for key, value in freq.items():
        print(f"{key} appears : {value} times.")
# It takes O(n) time and O(n) space
def freq_count_better_alt(arr):
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1
    for key, value in freq.items():
        print(f"{key} appears : {value} times.")
# It takes O(n) time and O(n) extra space
def freq_count(arr):
    freq = Counter(arr)
    for key, value in freq.items():
        print(f"{key} appears : {value} times.")
# It takes time : O(n) and O(n) extra space
def main():
    arr = [10, 5, 10, 15, 10, 5]
    freq_count(arr)
if __name__ == "__main__":
    main()
