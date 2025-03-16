def insertion_sort(arr, n):
    if n <= 1:
        return
    insertion_sort(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    #####################
def main():
    arr = [13,46,24,52,20,9]
    n = len(arr)
    insertion_sort(arr, n)
    print(arr)
#####################
if __name__ == "__main__":
    main()
