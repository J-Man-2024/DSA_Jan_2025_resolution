# Problem : Given array find the length of the max sub array of sum k.

# brute force
def sum_of_max_sub_arr_brute(arr, k):
    max_len = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == k:
                max_len = max(max_len, j - i + 1)
    return max_len
# It takes O(n^2) and O(1) extra space

def sum_of_max_sub_arr_better(arr, k):
    prefix_sum = 0
    max_len = 0
    prefix_hashmap = {0: -1}

    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum - k in prefix_hashmap:
            max_len = max(max_len, i - prefix_hashmap[prefix_sum - k])
        if prefix_sum not in prefix_hashmap:
            prefix_hashmap[prefix_sum] = i
    return max_len
# It takes O(n) and O(n) extra space due to hashmap

def sum_of_max_sub_arr_best(arr, k):
    left = 0
    curr_sum = 0
    max_len = 0
    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum > k and left <= right:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == k:
            max_len = max(max_len, right - left + 1)
    return max_len
# It takes O(2n) and O(1) only for positives.
def main():
    arr = [9, 1, 5, 3, 2]
    k = 10
    solution = sum_of_max_sub_arr_best(arr, k)
    print(solution)

if __name__ == "__main__":
    main()
