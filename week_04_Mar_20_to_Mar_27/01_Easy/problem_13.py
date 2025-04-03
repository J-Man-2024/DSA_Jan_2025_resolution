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

def main():
    arr = [9, 1, 5, 3, 2]
    k = 10
    solution = sum_of_max_sub_arr_brute(arr, k)
    print(solution)

if __name__ == "__main__":
    main()
