def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def main():
    arr = [13,46,24,52,20,9]
    n = len(arr)
    insertion_sort(arr, n)
    print(arr)
if __name__ == "__main__":
    main()
