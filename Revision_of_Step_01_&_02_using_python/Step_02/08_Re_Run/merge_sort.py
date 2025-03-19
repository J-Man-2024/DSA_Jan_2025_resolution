def merge(arr, low, mid, high):
    sorted_arr = []
    leftIndex = low
    rightIndex = mid + 1

    while leftIndex <= mid and rightIndex <= high:
        if arr[leftIndex] <= arr[rightIndex]:
            sorted_arr.append(arr[leftIndex])
            leftIndex += 1
        else:
            sorted_arr.append(arr[rightIndex])
            rightIndex += 1
    while leftIndex <= mid:
        sorted_arr.append(arr[leftIndex])
        leftIndex += 1
    while rightIndex <= high:
        sorted_arr.append(arr[rightIndex])
        rightIndex += 1

    for i in range(len(sorted_arr)):
        arr[low + i] = sorted_arr[i]
def merge_sort(arr, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
def main():
    arr = [13,46,24,52,20,9]
    n = len(arr)
    merge_sort(arr, 0, n - 1)
    print(arr)
if __name__ == "__main__":
    main()
