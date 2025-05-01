def selection_sort(arr, n):
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
# It takes O(n^2) time and O(1) extra space
def bubble_sort(arr, n):
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
        if not swapped:
            break
# It takes O(n^2) time and O(1) extra space
def insertion_sort(arr, n):
    for i in range(1, n):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
# It takes O(n^2) time and O(1) extra space
def merge(arr, start, mid, end):
    temp = []
    left_index = start
    right_index = mid + 1

    while left_index <= mid and right_index <= end:
        if arr[left_index] <= arr[right_index]:
            temp.append(arr[left_index])
            left_index += 1
        else:
            temp.append(arr[right_index])
            right_index += 1
    while left_index <= mid:
        temp.append(arr[left_index])
        left_index += 1
    while right_index <= end:
        temp.append(arr[right_index])
        right_index += 1
    for i in range(len(temp)):
        arr[start + i] = temp[i]
    
def merge_sort(arr, start, end):
    if start < end:
        pi = start + (end - start) // 2
        merge_sort(arr, start, pi)
        merge_sort(arr, pi + 1, end)
        merge(arr, start, pi, end)
# It takes O(nlogn) time and O(n) extra space
def recursive_bubble_sort(arr, n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    recursive_bubble_sort(arr, n - 1)
#   It takes O(n^2) and O(n) extra space
def recursive_insertion_sort(arr, n):
    if n <= 1:
        return
    recursive_insertion_sort(arr, n - 1)
    j = n - 2
    key = arr[n - 1]
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
# It takes O(n^2) time and O(n) extra space
def partition_index(arr, start, end):
    pivot = arr[start]
    start_index = start
    end_index = end
    while start_index < end_index:
        while start_index <= end and arr[start_index] <= pivot:
            start_index += 1
        while end_index >= start and arr[end_index] > pivot:
            end_index -= 1
        if start_index < end_index:
            arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
    arr[start], arr[end_index] = arr[end_index], arr[start]
    return end_index

def quick_sort(arr, start, end):
    if start < end:
        pi = partition_index(arr, start, end)
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)
# It takes O(nlogn) time and O(1) extra space
def main():
    arr = [13, 46, 24, 52, 20, 9]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print(arr)
if __name__ == "__main__":
    main()
