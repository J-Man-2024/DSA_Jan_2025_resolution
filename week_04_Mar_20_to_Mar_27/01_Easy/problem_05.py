# Problem : Rotate the array left by one place.
# Brute force:
def rotate_left_brute(arr):
    n = len(arr)
    if n < 2:
        return arr
    new_array = [0] * n
    for i in range(1, n):
        new_array[i - 1] = arr[i]
    new_array[n - 1] = arr[0]
    return new_array
# It takes O(n) time and O(n) extra space because of new array.
def rotate_left_optimal(arr):
    n = len(arr)
    if n < 2:
        return arr
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
    return arr
# It takes time O(n) and O(1) extra space because we're not creating a new array just a variable.

def main():
    arr = [1, 2, 3, 4, 5]
    new_array = rotate_left_optimal(arr)
    print(new_array)

if __name__ == "__main__":
    main()
