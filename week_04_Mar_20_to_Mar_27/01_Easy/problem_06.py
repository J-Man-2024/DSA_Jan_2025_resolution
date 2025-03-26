# Problem: Rotate array by D places
# Brute force
def rotate_left_or_right_d_places_brute(arr, rotate, d):
    n = len(arr)
    if n < 2 or d == 0:
        return arr
    d = d % n
    temp_array = [0] * n 
    if rotate == "right":
        for i in range(n - d, n):
            temp_array[i - (n - d)] = arr[i]
        for i in range(0, n - d):
            temp_array[d + i] = arr[i] 
    elif rotate == "left":
        for i in range(d, n):
            temp_array[i - d] = arr[i]
        for i in range(0, d):
            temp_array[n - d + i] = arr[i]
    else:
        raise ValueError("Rotation value must be either 'right' or 'left'.")
    return temp_array
def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    rotate = "left"
    rotated_array = rotate_left_or_right_d_places_brute(arr,rotate, d)
    print(rotated_array)
if __name__ == "__main__":
    main()
