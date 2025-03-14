arr = [5, 4, 3, 2, 1]
n = len(arr)
for i in range(n - 1):
    minIndex = i
    for j in range(i + 1, n):
        if arr[j] < arr[minIndex]:
            minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]

print(arr)
