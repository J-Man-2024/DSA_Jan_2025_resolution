def rotate_array_brute(arr, k, direction):
    n = len(arr)
    if n == 0:
        return
    rotation = k % n
    if rotation > n:
        return 
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
def main():
    arr = [1,2,3,4,5,6,7]
    k = 1
    direction = 'left'
    print(rotate_array_brute(arr, k, direction))
if __name__ == "__main__":
    main()
