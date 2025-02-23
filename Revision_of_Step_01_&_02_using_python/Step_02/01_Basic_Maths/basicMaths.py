import math

def problem01BruteForce(n):
    count = 0
    while n:
        count+=1
        n = n // 10
    return count

def problem01Optimized(n):
    count = int(math.log10(n)+1)
    return count
    
def problem02(n):
    revNum = 0
    while n:
        lastDigit = n % 10
        revNum = revNum * 10 + lastDigit
        n = n // 10
    return revNum

def problem03(n):
    cpy = n
    revNum = 0
    
    while n:
        lastDigit = n % 10
        revNum = revNum * 10 + lastDigit
        n = n // 10
    if cpy == revNum:
        return True
    else:
        return False

def problem04BruteForce(n1,n2):
    n = min(n1,n2)
    gcd = 1

    for i in range(1,n+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd
    
def problem04BetterApproach(n1,n2):
    n = min(n1,n2)
    for i in range(n, 0 ,-1):
        if n1 % i == 0 and n2 % i == 0:
           return i 

def problem04Optimized(n1,n2):
    a = n1
    b = n2
    
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        elif b > a:
            b = b % a

    if a == 0:
        return b

    return a

def problem05(n):
    cpy = n
    length = len(str(abs(n)))
    sum = 0
    
    while n:
        lastDigit = n % 10
        sum = (lastDigit ** length) + sum
        n = n // 10

    print(sum)
    print()
    
    if sum == cpy:
        return True
    else:
        return False
##################
def main():
    n = 371
    print(problem05(n))

if __name__ == "__main__":
    main()
