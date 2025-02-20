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
##################
def main():
    n = 4554
    print(problem03(n))

if __name__ == "__main__":
    main()
