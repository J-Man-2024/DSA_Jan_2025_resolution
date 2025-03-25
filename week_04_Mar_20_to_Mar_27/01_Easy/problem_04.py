# Problem: Remove Duplicates in-place from sorted array.
# Brute force
def remove_duplicates_brute_in_place(arr):
    if not arr:
        return 0
    unique_elements = sorted(set(arr))
    for i in range(len(unique_elements)):
        arr[i] = unique_elements[i]
    return len(unique_elements)
# it takes O(n) for loop and O(nlogn) for sorting overall O(nlogn) and time O(1)

def remove_duplicates_brute(arr):
    if not arr:
        return []
    unique_elements = sorted(set(arr))
    return unique_elements
#it takes O(nlogn) overall and O(n) extra space due to new array

def remove_duplicates_optimal_in_place(arr):
    if not arr:
        return 0
    index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]
    return index + 1
# It takes overall O(n) time and O(1) extra space

def remove_duplicates_optimal(arr):
    if not arr:
        return []

    unique_elements = []
    unique_elements.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_elements.append(arr[i])
    return unique_elements        
# It takes overall O(n) and O(n) extra space due to new array for storing unique elements                
def main():
    arr = [1,1,2,2,2,3,3]
    new_length = remove_duplicates_optimal(arr)
    print(f"The number of unique elements are : {len(new_length)} and the array is: {new_length}")
if __name__ == "__main__":
    main()
