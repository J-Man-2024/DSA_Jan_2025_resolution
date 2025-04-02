# Given a non-empty array of integers arr, every element appears twice except for one.
# Find that single one.

# Brute force
def appears_once_brute(arr):
    for i in range(len(arr)):
        count = 0
        for num in arr:
            if arr[i] == num:
                count += 1
        if count == 1:
            return arr[i]
    return None
# It takes O(n^2) and O(1) extra space

def appears_once_better(arr):
    max_element = max(arr)
    hash = [0] * (max_element + 1)
    for num in arr:
        hash[num] += 1
    for num in hash:
        if hash[num] == 1:
            return num  
    return None
# It takes O(n) + O(n) + O(max_element) and space O(max_element + 1)

def appears_once_better_alt(arr):
    map = {}
    for num in arr:
        map[num] = map.get(num, 0) + 1
    for key, value in map.items():
        if value == 1:
            return key
    return None
# It takes O(n) + O(n) and O(n) extra space

def appears_once_optimal(arr):
    if not arr:
        return None
    result = 0
    for num in arr:
        result ^= num
    return result if result in arr else None
# It takes O(n) and O(1) extra space

def main():
    arr = [2, 2, 1]
    new_arr = appears_once_optimal(arr)
    print(f"In array {arr} : {new_arr} appears once.")
if __name__ == "__main__":
    main()
 
