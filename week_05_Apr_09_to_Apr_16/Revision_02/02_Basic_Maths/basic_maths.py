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

def armstrong_brute(n):
    length = len(str(n))
    temp = n
    sum = 0
    while n > 0:
        ld = n % 10
        sum += pow(ld,length)
        n //= 10
    if sum == temp:
        return True
    return False
# It takes O(logbase10n + 1) time and O(1) extra space

def all_divisors_brute(n):
    temp = []
    for i in range(1, n + 1):
        if n % i == 0:
            temp.append(i)
    return temp
# It takes O(n) time and O(n) extra space

def all_divisors_optimal(n):
    temp = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            temp.append(i)
            if n // i != i:
                temp.append(n // i)
    return sorted(temp)
# It takes O(sqrt(n)) if unsorted otherwise O(sqrt(n)logn) and O(sqrt(n))

def prime_or_not_brute(n):
    if n < 2:
        return False
    count = 0 
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
# It takes O(n) time and O(1) extra space

def prime_or_not_optimal(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# It takes O(sqrt(n)) time and O(1)
def main():
    n = 36
    print(prime_or_not_optimal(n))
if __name__ == "__main__":
    main()
