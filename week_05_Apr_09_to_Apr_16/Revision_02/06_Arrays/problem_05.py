def left_rotate_brute(arr):
    n = len(arr)
    temp_arr = [0] * n
    for i in range(1, n):
        temp_arr[i - 1] = arr[i]
    temp_arr[n - 1] = arr[0]
    return temp_arr
#   It takes O(n) time and O(n) space
def left_rotate_better(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
    return arr
#   It takes O(n) time and O(1) space
def right_rotate(arr):
    n = len(arr)
    temp = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = temp
    return arr
def main():
    arr = [1, 2, 3, 4, 5]
    print(right_rotate(arr))
if __name__ == "__main__":
    main()
