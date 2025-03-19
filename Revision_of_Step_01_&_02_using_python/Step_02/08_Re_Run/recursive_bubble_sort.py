def bubble_sort(arr, n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort(arr, n - 1)
def main():
    arr = [13,46,24,52,20,9]
    n = len(arr)
    bubble_sort(arr, n)
    print(arr)
if __name__ == "__main__":
    main()
