def largest_element_brute(arr):
    arr.sort() #Tim sort
    return arr[-1]
# It takes O(nlogn) time and O(logn) extra space due to recursion stack
def largest_element_better(arr):
    largest_element = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest_element:
            largest_element = arr[i]
    return largest_element
# It takes O(n) time and O(1) extra space

def main():
    arr = [2, 5, 1, 3, 0]
    print(largest_element_better(arr))
if __name__ == "__main__":
    main()
