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
def main():
    arr = [13, 46, 24, 52, 20, 9]
    n = len(arr)
    insertion_sort(arr, n)
    print(arr)
if __name__ == "__main__":
    main()
