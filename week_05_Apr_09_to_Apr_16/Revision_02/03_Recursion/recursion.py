
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)

def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)

def sum_of_n_num(n):
    if n == 0:
        return 0
    return n + sum_of_n_num(n - 1)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def reverse_arr(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverse_arr(arr, start + 1, end - 1)
def main():
    arr = [1,2,3,4,5]
    n = len(arr)
    reverse_arr(arr, 0, n - 1)
    print(arr)

if __name__ == "__main__":
    main()
