import math

def problem01BruteForce(n):
    count = 0
    while(n):
        count+=1
        n = n // 10
    return count

def problem01Optimized(n):
    count = int(math.log10(n)+1)
    return count
    
    
##################
def main():
    n = 12345 
    ans = problem01Optimized(n)
    print(f"The number of digits in \"{n}\" is : {ans}.")


if __name__ == "__main__":
    main()
