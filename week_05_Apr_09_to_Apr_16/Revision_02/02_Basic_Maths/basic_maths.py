import math
def count_digits_brute(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count
# It takes O(logbase10n) time and O(1) extra space

def count_digits_better(n):
    return (int(math.log10(n) + 1))
# It takes O(1) time and O(1) extra space

def reverse_a_number(n):
    rev_num = 0
    while n > 0:
        ld = n % 10
        rev_num = rev_num * 10 + ld
        n //= 10
    return rev_num
# It takes O(logbase10n + 1) time and O(1) extra space
def palindrome_or_not(n):
    og_num = n
    rev_num = 0
    while n > 0:
        ld = n % 10
        rev_num = rev_num * 10 + ld
        n //= 10
    if og_num == rev_num:
        return True
    return False
# It takes O(logbase10n + 1) time and O(1) extra space

def gcd_brute(n1, n2):
    n = min(n1, n2)
    gcd = 1
    for i in range(1, n + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd
# It takes O(min(n1,n2)) and O(1) extra space

def gcd_better(n1, n2):
    n = min(n1, n2)
    for i in range(n, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i
    return 1
# It takes O(min(n1, n2)) and O(1) extra space but has fewer iteration for the worst case.

def gcd_optimal(n1, n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 %= n2
        else:
            n2 %= n1
    if n1 == 0:
        return n2
    return n1

# It takes O(min(n1, n2)) time and O(1) extra space
def main():
    n1 = 9
    n2 = 12
    print(gcd_optimal(n1, n2))

if __name__ == "__main__":
    main()
