def problem01(n):
    if n == 0:
        return
    problem01(n-1)
    print(n,end=" ")

def problem02(n):
    if n == 0:
        return
    print(n,end=" ")
    problem02(n-1)

def problem03(n):
    if n == 0:
        return 0
    return problem03(n-1)+n

def problem04(n):
    if n == 0:
        return 1
    return problem04(n-1)*n

def problem05(arr,start,end):
    if start < end:
        arr[start],arr[end] = arr[end],arr[start]
        problem05(arr,start+1,end-1)

def problem06(s,start,end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return problem06(s,start+1,end-1)

def problem07(n):
    if n <= 1:
        return n
    return problem07(n-1) + problem07(n-2)
##__main function__##
def main():
    n = 5
    print(" ".join(str(problem07(i)) for i in range(n+1)))
##__calling main function__##
if __name__ == "__main__":
    main()
