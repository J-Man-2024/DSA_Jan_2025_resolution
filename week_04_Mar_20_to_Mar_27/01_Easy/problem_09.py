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
# It takes O(n + m)
def union_of_arrays_best(arr1, arr2):
    union = []
    i = j = 0
    n , m = len(arr1), len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1
    while i < n:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    while j < m:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    return union
# It takes O(n + m) and O(n + m) extra space for union array otherwise O(1) to solve
def union_of_arrays_best_alt(arr1, arr2):
    return list(set(arr1) | set(arr2))
# It takes O(n + m) and O(n + m) extra space
def main():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 3, 4, 4, 5]
    union_of_arr = union_of_arrays_best_alt(arr1, arr2)
    print(union_of_arr)

if __name__ == "__main__":
    main()
