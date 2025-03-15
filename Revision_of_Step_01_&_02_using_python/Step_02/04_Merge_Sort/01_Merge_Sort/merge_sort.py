def merge(arr, start, mid, end):
    leftIndex = start
    rightIndex = mid + 1
    sorted_arr = []

    while leftIndex <= mid and rightIndex <= end:
        if arr[leftIndex] <= arr[rightIndex]:
            sorted_arr.append(arr[leftIndex])
            leftIndex += 1
        else:
            sorted_arr.append(arr[rightIndex])
            rightIndex += 1
    
    while leftIndex <= mid:
        sorted_arr.append(arr[leftIndex])
        leftIndex += 1
    while rightIndex <= end:
        sorted_arr.append(arr[rightIndex])
        rightIndex += 1

    for i in range(len(sorted_arr)):
        arr[start + i] = sorted_arr[i]

def merge_sort(arr, start, end):
    if start < end:
        mid = start + (end - start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

###############
def main():
    arr = [4, 2, 1, 6, 7]
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)


###############
if __name__ == "__main__":
    main()
