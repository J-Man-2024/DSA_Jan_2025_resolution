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

def problem06(arr,start,end):
    if start >= end:
        return True
    if arr[start] != arr[end]:
        return False
    return problem06(arr, start+1, end-1)

def problem07(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return problem07(s, start+1, end-1)

def problem08(n):
    if n <= 1:
        return n
    return problem08(n - 1) + problem08(n - 2)

###################
def main():
    n = 5
    print(" ".join(str(problem08(i)) for i in range(n+1)))

###################
if __name__ == "__main__":
    main()
