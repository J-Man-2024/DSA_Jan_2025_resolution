def pattern01(n):
    for i in range(n):
        print("".join("*")*n)

def pattern02(n):
    for i in range(n):
        print("".join("*")*(i+1))

def pattern03(n):
    for i in range(1,n+1):
        print("".join(map(str,range(1,i+1))))

def pattern04(n):
    for i in range(1,n+1):
        print("".join(str(i))*i)

def pattern05(n):
    for i in range(n,0,-1):
        print("*"*i)

def pattern06(n):
    for i in range(n,0,-1):
        print("".join(map(str,range(1,i+1))))

def pattern07(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * (i *2 -1))

def pattern08(n):
    for i in range(0,n):
        print(" " * i + "*" * (2*(n-i)-1))

def pattern09(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * (i*2-1))
    for i in range(0,n):
        print(" " * i + "*" * (2*(n-i)-1))

def pattern10(n):
    for i in range(1,n*2):
        stars = i if i < n else (n*2-i)
        print("*" * stars)

def pattern11(n):
    for i in range(1,n+1):
        print(" ".join("1" if i % 2 == j % 2 else "0" for j in range(1,i+1)))

def pattern12(n):
    for i in range(1,n+1):
        print("".join(map(str,range(1,i+1))) + " " * (2 * (n-i))+ "".join(map(str, range(i,0,-1))))

def pattern13(n):
    count=1;
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(count,end=" ")
            count += 1
        print()

def pattern13Concise(n):
    count=1
    for i in range(1,n+1):
        print(" ".join(str(count+j) for j in range(i)))
        count += i

def pattern14(n):
    for i in range(1,n+1):
        print("".join(chr(c) for c in range(65,65+i)))

def pattern15(n):
    for i in range(n,0,-1):
        print("".join(chr(c) for c in range(65, 65+i)))

def pattern16(n):
    for i in range(1, n+1):
        print(chr(65+i-1)*i)

def pattern17(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "".join(chr(c) for c in range(65,65+i)) + "".join(chr(c) for c in range(64+i-1,64,-1)))

def pattern18(n):
    for i in range(1,n+1):
        print(" ".join(chr(c) for c in range(65+n-i,65+n)))

def pattern19(n):
    for i in range(n):
        print("*" * (n-i) + " " * (i * 2) + "*" * (n-i))
    for i in range(1,n+1):
        print("*" * i + " " * (2*(n-i)) + "*" * i)

def pattern20(n):
    for i in range(1,n*2):
        stars = i if i < n else 2*n-i
        spaces = 2*(n-stars) 
        print("*" * stars + " " * spaces + "*" * stars)

def pattern21(n):
    for i in range(n):
        print("".join("*" if i in {0,n-1} or j in {0,n-1} else " " for j in range(n)))

def pattern22(n):
    start = n*2-1
    for i in range(start):
       print(" ".join(str(n - min(i,j,start-i-1,start-j-1)) for j in range(start)))

######################
def main():
    n = 5
    pattern22(n)

if __name__ == "__main__":
    main()
