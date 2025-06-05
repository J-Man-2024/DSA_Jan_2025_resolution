def mov_zeros_to_the_end_brute(arr, n):
    if n == 0:
        return arr
    temp_arr = [0] * n
    count = 0
    for i in range(n):
        if arr[i] != 0:
            temp_arr[count] = arr[i]
            count += 1
    return temp_arr
# It takes O(n) time and O(n) extra space
def mov_zeros_to_the_end_better(arr, n):
    if n == 0:
        return arr
    result = []
    zero_count = 0
    for num in arr:
        if num != 0:
            result.append(num)
        else:
            zero_count += 1
    result.extend([0] * zero_count)
    return result
# It takes O(n) time and O(n) extra space
def mov_zeros_to_the_end_optimal(arr, n):
    if n == 0:
        return arr
    last_non_zero = 0
    for i in range(n):
        if arr[i] != 0:
            arr[last_non_zero], arr[i] = arr[i], arr[last_non_zero]
            last_non_zero += 1
    return arr
# It takes O(n) time and O(1) extra space
def main():
    arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
    n = len(arr)
    print(mov_zeros_to_the_end_optimal(arr, n))
if __name__ == "__main__":
    main()