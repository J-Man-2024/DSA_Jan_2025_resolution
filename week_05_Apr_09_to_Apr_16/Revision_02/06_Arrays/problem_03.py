def sorted_or_not_brute(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False
    return True
#   It takes O(n^2) time and O(1) space
def sorted_or_not_better(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
#   It takes O(n) time and O(1) space
def main():
    arr = [1,2,3,4,5]
    print(sorted_or_not_brute(arr))
if __name__ == "__main__":
    main()
