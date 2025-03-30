# Problem : Find the missing number in an array
# brute force

def missing_number_brute(arr):
    
    for i in range(1, len(arr) + 1):
        flag = 0
        for j in range(len(arr)):
            if arr[j] == i:
                flag = 1                         
                break
        if flag == 0:
            return i
    return -1
# It takes O(n^2) and O(1) space

def missing_number_better(arr):
    n = len(arr)
    hmap = [0] * (n + 1)
    for i in range(n - 1):
        hmap[arr[i]] += 1
    for i in range(1, n + 1):
        if hmap[i] == 0:
            return i
    return -1
# It takes O(n + n) and O(n) extra space

def missing_number_best(arr):
    n = len(arr) + 1
    expected_total = (n * (n + 1) // 2)
    current_total = sum(arr)
    return expected_total - current_total 

def main():
    arr = [1, 2, 4, 5]
    new_arr = missing_number_best(arr)
    print(f"Missing number in {arr} is : {new_arr}")
if __name__ == "__main__":
    main()
