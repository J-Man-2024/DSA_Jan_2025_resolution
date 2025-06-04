def rotate_arr_brute(arr, k, direction):
    n = len(arr)
    if n == 0:
        return arr
    rotation = k % n
    temp_arr = [0] * n
    if direction == 'right':
        for i in range(n - rotation, n):
            temp_arr[i + rotation - n] = arr[i]
        for i in range(n - rotation):
            temp_arr[i + rotation] = arr[i]
    elif direction == 'left':
        for i in range(rotation, n):
            temp_arr[i - rotation] = arr[i]
        for i in range(rotation):
            temp_arr[n - rotation + i] = arr[i]
    return temp_arr
# It takes O(n) time and O(n) space
def arr_rotation(arr, start, end):
    n = len(arr)
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
def rotate_arr_optimal(arr, k, direction):
    n = len(arr)
    if n == 0:
        return arr
    rotation = k % n
    if direction == 'right':
        arr_rotation(arr, n - rotation, n - 1)
        arr_rotation(arr, 0, n - rotation - 1)
        arr_rotation(arr, 0, n - 1)
    elif direction == 'left':
        arr_rotation(arr, 0, rotation - 1)
        arr_rotation(arr, rotation, n - 1)
        arr_rotation(arr, 0, n - 1)
    return arr
# It takes O(n) time and O(1) extra space
def main():
    arr = [1,2,3,4,5,6,7]
    k = 2
    direction = 'left'
    print(rotate_arr_optimal(arr, k, direction))
if __name__ == "__main__":
    main()
