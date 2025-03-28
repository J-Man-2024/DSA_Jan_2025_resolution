# Problem : union of two sorted arrays.
# brute force

def union_of_arrays_brute(arr1, arr2):
    freq = {}
    union = []

    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    for num in arr2:
        freq[num] = freq.get(num, 0) + 1
    for num in freq:
        union.append(num)
    return sorted(union)
# It takes O((n + m)log(n + m))

def union_of_arrays_better(arr1, arr2):
    s = set()
    union = []
    for num in arr1:
        s.add(num)
    for num in arr2:
        s.add(num)
    for num in s:
        union.append(num)
    return union

def main():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 3, 4, 4, 5]
    union_of_arr = union_of_arrays_better(arr1, arr2)
    print(union_of_arr)

if __name__ == "__main__":
    main()
