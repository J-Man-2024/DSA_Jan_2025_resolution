# Problem : Move all zeros to the end of the array
# Brute force
def move_zeros_to_end_brute(arr):
    n = len(arr)
    if n < 2:
        return arr
    temp_arr = [0] * n
    index = 0
    for i in range(n):
        if arr[i] != 0:
            temp_arr[index] = arr[i]
            index += 1
    return temp_arr
# It takes time : O(n) and O(n) extra space due to temp arr.
def move_zeros_to_end_optimal(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1
    return arr
# It takes time : O(n) and O(1) extra space.
def main():
    arr = [1, 0, 2, 3, 0, 4, 0, 1]
    new_arr = move_zeros_to_end_optimal(arr)
    print(new_arr)
if __name__ == "__main__":
    main()
