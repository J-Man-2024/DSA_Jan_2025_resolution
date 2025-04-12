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
    gcd = []
    for i in range(1, n + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd.append(i)
    return max(gcd)    

def main():
    n1 = 9
    n2 = 12
    print(gcd_brute(n1, n2))

if __name__ == "__main__":
    main()
