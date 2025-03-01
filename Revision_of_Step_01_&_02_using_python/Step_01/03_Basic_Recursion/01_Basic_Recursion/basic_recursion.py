import math

def problem01(n):
    if n == 0 :
        return
    problem01(n-1)
    print(n)

def problem02(n):
    if n == 0:
        return
    print(n)
    problem02(n-1)

def problem03(n):
    if n == 0:
        return 0
    return n + problem03(n-1)

def problem04(n):
    if n < 1:
        return 1
    return n * problem04(n-1)

def problem05(arr,start,end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        problem05(arr,start+1,end-1)

###################
def main():
    arr = [1,2,3,4,5]
    n = len(arr)
    problem05(arr, 0, n-1)
    print(arr)

###################
if __name__ == "__main__":
    main()
