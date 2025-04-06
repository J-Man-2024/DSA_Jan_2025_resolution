# Problem : Longest subarray with sum K | [Positives and Negatives]

#brute force
def longest_subarray_brute(arr, k):
    max_len = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == k:
                max_len = max(max_len, j - i + 1)
    return max_len
# It takes O(n^2) and O(1) extra space

def longest_subarray_optimal(arr, k):
    max_len = 0
    prefix_sum = 0
    prefix_map = {0 : -1}

    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum - k in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    return max_len
# It takes O(n) and O(n) extra space
def main():
    arr = [-1, 1, 1]
    k = 1
    solution = longest_subarray_optimal(arr, k)
    print(solution)
if __name__ == "__main__":
    main()
