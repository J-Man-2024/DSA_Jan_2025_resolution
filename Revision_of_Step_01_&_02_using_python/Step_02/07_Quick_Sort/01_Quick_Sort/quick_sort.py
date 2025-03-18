def partition(arr, start, end):
    pivot = arr[start]
    lowIndex = start
    highIndex = end

    while lowIndex < highIndex:
        while lowIndex <= end and arr[lowIndex] <= pivot:
            lowIndex += 1
        while highIndex >= start and arr[highIndex] > pivot:
            highIndex -= 1
        if lowIndex < highIndex:
            arr[lowIndex], arr[highIndex] = arr[highIndex], arr[lowIndex]
    arr[start], arr[highIndex] = arr[highIndex], arr[start]
    return highIndex

def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)

###############
def main():
    arr = [4,1,7,9,3]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print(arr)
###############
if __name__ == "__main__":
    main()
