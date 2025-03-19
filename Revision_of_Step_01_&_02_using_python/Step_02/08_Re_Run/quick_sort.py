def partition(arr, low, high):
    startIndex = low
    endIndex = high
    pivot = arr[low]

    while startIndex < endIndex:
        while startIndex <= high and arr[startIndex] <= pivot:
            startIndex += 1
        while endIndex >= low and arr[endIndex] > pivot:
            endIndex -= 1
        if startIndex < endIndex:
            arr[startIndex], arr[endIndex] = arr[endIndex], arr[startIndex]
    arr[low], arr[endIndex] = arr[endIndex], arr[low] 
    return endIndex
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
def main():
    arr = [4,6,2,5,7,9,1,3]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print(arr)
if __name__ == "__main__":
    main()
