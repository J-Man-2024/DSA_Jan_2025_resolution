def union_of_arrays_brute(arr1, arr2):
    result = []
    for num in arr1:
        if num not in result:
            result.append(num)
    for num in arr2:
        if num not in result:
            result.append(num)
    return result
# It takes O(n * k1 + m * k2) => O(n + m)^2 time and O(k1 + k2) space
def union_of_arrays_better(arr1, arr2):
#     using Hash map (dict)
    freq = {}
    result = []
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    for num in arr2:
        freq[num] = freq.get(num, 0) + 1
    for num in freq:
        result.append(num)
    return result
# It takes O(n + m) time and O(n + m) space
def main():
    arr1 = [1,2,3,4,5]
    arr2 = [2,3,4,4,5]
    print(union_of_arrays_better(arr1, arr2))
if __name__ == "__main__":
    main()