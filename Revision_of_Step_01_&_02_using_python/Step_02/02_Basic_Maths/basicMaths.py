import math

def problem01BruteForce(n):
    count = 0
    while n:
        count+=1
        n = n // 10
    return count

def problem01Optimized(n):
    count = int(math.log10(n) + 1)
    return count

def problem02(n):
    revNum = 0
    while n:
        ld = n % 10
        revNum = revNum * 10 + ld
        n = n // 10
    return revNum

def problem03(n):
    cpy = n
    revNum = 0
    while n:
        ld = n % 10
        revNum = revNum * 10 + ld
        n = n // 10

    if revNum == cpy:
        return True
    else:
        return False

def problem04BruteForce(n1,n2):
    n = min(n1,n2)
    gcd = 0
    for i in range(1, n+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

def problem04BruteForceAlt(n1,n2):
    n = min(n1,n2)
    gcd = 0
    for i in range(n, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i
    return 1

def problem04Optimized(n1,n2):
    a, b = n1, n2

    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b

    return a

def problem05(n):
    length = len(str(n))
    sum = 0
    cpy = n
    while n:
        ld = n % 10
        sum += ld ** length
        n = n // 10
    if sum == cpy:
        return True

    return False

def problem06BruteForce(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sorted(divisors)

def problem06(n):
    divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return sorted(divisors)

def problem07BruteForce(n):
    if n < 2:
        return False

    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

def problem07(n):
    if n < 2:
        return False
    count = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1

    if count == 2:
        return True
    else:
        return False
#####################
def main():
    n = 4
    print(problem07(n))

#####################
if __name__ ==  "__main__":
    main()
