def bubble_sort(arr, n):
    for i in range(n-1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

###############3
def main():
    arr = [13,46,24,52,20,9]
    n = len(arr)
    bubble_sort(arr, n)
    print(arr)

###############
if __name__ == "__main__":
    main()
