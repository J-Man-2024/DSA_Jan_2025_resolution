from collections import Counter
from collections import defaultdict
import math

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
# It takes O(n^2) time and O(n) extra space
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

def high_or_low_brute(arr):
    n = len(arr)
    freq = [False] * n
    max_freq = -1
    max_value = None
    min_value = None
    min_freq = n
    for i in range(n):
        if freq[i] == True:
            continue
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
                freq[j] = True
        if count > max_freq:
            max_freq = count
            max_value = arr[i]
        elif count < min_freq:
            min_freq = count
            min_value = arr[i]
    print(f"Max =>{max_value} appears : {max_freq}\nMin =>{min_value} appears : {min_freq}")
# It takes O(n^2) times and O(n) extra space

def high_or_low(arr):
    n = len(arr)
    freq = {}
    high_freq = 0
    low_freq = n
    high_freq_value = None
    low_freq_value = None
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for key, value in freq.items():
        if value > high_freq:
            high_freq = value
            high_freq_value = key
        elif value < low_freq:
            low_freq = value
            low_freq_value = key
    print(f"High Freq => {high_freq_value} appears : {high_freq} times.\nLow Freq => {low_freq_value} appears : {low_freq} times.")
# It takes O(n+n) and O(n) extra space

def main():
    arr = [10, 5, 10, 15, 10, 5]
    high_or_low(arr)
if __name__ == "__main__":
    main()
