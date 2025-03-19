def selection_sort(arr, n):
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
def main():
    arr = [13,46,24,52,20,9]
    n = len(arr)
    selection_sort(arr, n)
    print(arr)
if __name__ == "__main__":
    main()
