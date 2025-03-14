def selection_sort(arr,n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
#####################
def main():
    arr = [13,46,24,52,20,9]
    n = len(arr)
    selection_sort(arr, n)
    print(arr)
####################
if __name__ == "__main__":
    main()
