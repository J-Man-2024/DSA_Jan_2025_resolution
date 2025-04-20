
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

def palindrome_or_not_string(arr, start, end):
    if start >= end:
        return True
    if arr[start] != arr[end]:
        return False
    return palindrome_or_not_string(arr, start + 1, end - 1)

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)
def main():
    n = 5
    print(" ".join(str(fibo(i)) for i in range(n + 1)))
if __name__ == "__main__":
    main()
