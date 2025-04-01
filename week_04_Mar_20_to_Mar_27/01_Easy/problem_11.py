# Problem : Count maximum consecutive one's in the array.
#brute force
def max_consecutive_one_brute(arr):
    max_count = 0
    for i in range(len(arr)):
        count = 0
        for j in range(i, len(arr)):
            if arr[j] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                break
    return max_count
# It takes time O(n^2) and O(1) extra space

def max_consecutive_one_optimal(arr):
    max_count = 0
    count = 0
    for num in arr:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
# It takes time : O(n) and O(1) extra space
def main():
    arr = [1, 1, 0, 1, 1, 1] 
    new_arr = max_consecutive_one_optimal(arr)
    print(f"In array : {arr} the maximum consecutive one's is : {new_arr}.")

if __name__ == "__main__":
    main()
