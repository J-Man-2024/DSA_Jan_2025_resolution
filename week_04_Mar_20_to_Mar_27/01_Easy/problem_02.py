# Problem: Find second smallest and second largest element in an array
# Brute force method:

def find_second_min_max(arr, n):
    if n == 1 or n == 0:
        return -1, -1
    arr = sorted(set(arr))
    print(f"min: {arr[1]}\nmax: {arr[-2]}")
#better approach
def find_second_min_max_better(arr, n):
    if n == 0 or n == 1:
        print(f"min: {-1}\nmax:{-1}")
def main():
    arr = [1,2,4,7,7,5]
    n = len(arr)
    find_second_min_max(arr, n)
if __name__ == "__main__":
    main()

