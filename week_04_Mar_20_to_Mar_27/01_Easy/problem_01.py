# Problem: Find the largest element in an array

def largestElement(arr, n):
    maxElement = arr[0]
    for i in range(n):
        if arr[i] > maxElement:
            maxElement = arr[i]
    return maxElement

def main():
    arr = [2, 0, 1, 3, 5]
    n = len(arr)
    print(largestElement(arr, n))

if __name__ == "__main__":
    main()
