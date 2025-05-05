def second_smallest_and_largest_brute(arr):
    if len(arr) < 2:
        return -1, -1
    first_small = second_small = float('inf')
    first_large = second_large = float('-inf')
    for i in range(len(arr)):
        first_small = min(first_small, arr[i])
        first_large = max(first_large, arr[i])
    for i in range(len(arr)):
        if arr[i] < second_small and arr[i] != first_small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != first_large:
            second_large = arr[i]
    return second_small, second_large
# It takes O(n) time and O(1) space
def second_smallest_and_largest_better(arr):
    if len(arr) < 2:
        return -1, -1
    first_small = second_small = float('inf')
    first_large = second_large = float('-inf')
    for i in range(len(arr)):
        if arr[i] < first_small:
            second_small = first_small
            first_small = arr[i]
        elif arr[i] < second_small and arr[i] != first_small:
            second_small = arr[i]
        if arr[i] > first_large:
            second_large = first_large
            first_large = arr[i]
        elif arr[i] > second_large and arr[i] != first_large:
            second_large = arr[i]
    return second_small, second_large
#   O(n) time and O(1) space
def main():
    arr = [1, 2, 4, 7, 7, 5]
    print(second_smallest_and_largest_better(arr))
if __name__ == "__main__":
    main()
