def bubble_sort(arr, n):
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
        if not swapped:
            break
def main():
    arr = [13,46,24,52,20,9]
    n = len(arr)
    bubble_sort(arr, n)
    print(arr)
if __name__ == "__main__":
    main()
