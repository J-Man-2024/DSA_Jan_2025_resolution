# Problem: Find second smallest and second largest element in an array
# Brute force method:

def find_second_min_max_brute(arr, n):
    if n == 0 or n == 1:
        print(f"second min:{-1}\nsecond max:{-1}")
    arr = sorted(set(arr))
    print(f"second min:{arr[1]}\nsecond max:{arr[-2]}")
# It will take O(n+nlogn) and O(1) because of sorted function and arr traversal for n times.

def find_second_min_max_better(arr, n):
    if n == 0 or n == 1:
        print(f"second min: {-1}\nsecond max: {-1}")
    firstMinElement, firstMaxElement = float('inf'), float('-inf')
    secondMinElement, secondMaxElement = float('inf'), float('-inf')

    for i in range(n):
        firstMinElement = min(arr[i], firstMinElement)
        firstMaxElement = max(arr[i], firstMaxElement)
    for i in range(n):
        if arr[i] < secondMinElement and arr[i] != firstMinElement:
            secondMinElement = arr[i]
        elif arr[i] > secondMaxElement and arr[i] != firstMaxElement:
            secondMaxElement = arr[i]
    print(f"second min: {secondMinElement}\nsecond max: {secondMaxElement}")
# It will take O(n + n) two traversal and O(1)

def find_second_min_max_optimal(arr, n):
    if n == 0 or n == 1:
        print(f"second min: {-1}\nsecond max: {-1}")
    firstMinElement, firstMaxElement = float('inf'), float('-inf')
    secondMinElement, secondMaxElement = float('inf'), float('-inf')

    for i in range(n):
        if arr[i] < firstMinElement:
            secondMinElement = firstMinElement
            firstMinElement = arr[i]
        elif arr[i] < secondMinElement and arr[i] != firstMinElement:
            secondMinElement = arr[i]
    for i in range(n):
        if arr[i] > firstMaxElement:
            secondMaxElement = firstMaxElement
            firstMaxElement = arr[i]
        elif arr[i] > secondMaxElement and arr[i] != firstMaxElement:
            secondMaxElement = arr[i]
    print(f"second min: {secondMinElement}\nsecond max: {secondMaxElement}")
# It will take O(n + n) and O(1) due to two traversal of the array
def main():
    arr = [1,2,4,7,7,5]
    n = len(arr)
    find_second_min_max_optimal(arr, n)
if __name__ == "__main__":
    main()

