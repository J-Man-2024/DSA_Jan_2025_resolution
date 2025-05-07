def remove_duplicates_brute(arr):
    visited = []
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        else:
            visited.append(arr[i])
    return visited
# It takes O(n^2) time and O(n) space
def remove_duplicates_better(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
# It takes O(n) time and O(n) space
def remove_duplicates_better_alt(arr):
    return list(dict.fromkeys(arr))
# It takes O(n) and O(n)
def remove_duplicates_best(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return arr[:i + 1]
# It takes O(n) time and O(1) space but it works only for sorted array 
def main():
    arr = [1,1,2,2,2,3,3]
    print(remove_duplicates_best(arr))
if __name__ == "__main__":
    main()
