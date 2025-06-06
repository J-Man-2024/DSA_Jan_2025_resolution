def linear_search(arr, num):
    n = len(arr)
    if n == 0:
        return 'array has no elements.'
    for i in range(n):
        if arr[i] == num:
            return i
    return 'Not found'
def main():
    arr = [5, 4, 3, 2, 1]
    num = 6
    print(linear_search(arr, num))
if __name__ == "__main__":
    main()