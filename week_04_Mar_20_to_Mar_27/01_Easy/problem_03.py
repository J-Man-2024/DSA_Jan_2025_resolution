# Problem: Check if array is sorted or not.
# Brute force

def isSortedBrute(arr, n):
    if n == 0 or n == 1:
        return True
    cpyArr = arr.copy()
    sortedArr = sorted(arr)
    if cpyArr == sortedArr:
        return True
    else:
        return False

def isSortedBrutePythonic(arr):
    return arr == sorted(arr)

def isSortedBruteTwoLoop(arr, n):
    if n == 0 or n == 1:
        return True
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False
    return True

def isSortedOptimal(arr, n):
    if n < 2:
        return True
    for i in range(n - 1):
        if arr[i]>arr[i + 1]:
            return False
    return True

def main():
    arr = [1,2,3,4,5]
    n = len(arr)
    print(isSortedOptimal(arr, n))

if __name__ == "__main__":
    main()
