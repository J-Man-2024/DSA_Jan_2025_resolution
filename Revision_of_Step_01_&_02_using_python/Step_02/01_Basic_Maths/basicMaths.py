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
    

##################
def main():
    n1 = 9
    n2 = 12
    print(problem04BruteForce(n1,n2))

if __name__ == "__main__":
    main()
