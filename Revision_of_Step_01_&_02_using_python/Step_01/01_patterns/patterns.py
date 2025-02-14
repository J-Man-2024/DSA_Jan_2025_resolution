def pattern01(n):
    for _ in range(n):
        print("* " * n)


def pattern02(n):
    for i in range(1, n+1):
        print("* " * i)

# verbose


def pattern03verbose(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()


def pattern03ConciseWithSpaces(n):
    for i in range(1, n+1):
        print(*range(1, i+1))


def pattern03ConciseWithoutSpaces(n):
    for i in range(1, n+1):
        print("".join(map(str, range(1, i+1))))


def pattern04(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end="")
        print()


def pattern04Concise(n):
    for i in range(1, n+1):
        print(str(i) * i)


def pattern05(n):
    for i in range(1, n+1):
        print("*" * (n-i+1))


def pattern05Alt(n):
    for i in range(n, 0, -1):
        print("*" * i)


def pattern06(n):
    for i in range(1, n+1):
        for j in range(1, n-i+2):
            print(j, end="")
        print()


def pattern06Concise(n):
    for i in range(n, 0, -1):
        print("".join(map(str, range(1, i+1))))


def pattern07Verbose(n):
    count = 1
    for i in range(1, n+1):
        for _ in range(n-i):
            print(" ", end="")
        for _ in range(count):
            print("*", end="")
        count = count+2
        print()


def pattern07Concise(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


def pattern08Verbose(n):
    count = n*2-1
    for i in range(1, n+1):
        for _ in range(1, i):
            print(" ", end="")
        for _ in range(count):
            print("*", end="")
        count -= 2
        print()


def pattern08Concise(n):
    for i in range(n):
        print(" "*i + "*"*(2*(n-i)-1))


def pattern09(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(2*i+1))
    for i in range(n):
        print(" "*i+"*"*(2*(n-i)-1))


def pattern10(n):
    for i in range(1, n*2):
        stars = 2*n-i if n < i else i
        print("*"*stars)


def pattern11Verbose(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if (i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 == 0):
                print("1 ", end="")
            else:
                print("0 ", end="")
        print()


def pattern11ConciseAlt(n):
    for i in range(1, n+1):
        print(" ".join("1" if ((i % 2 != 0 and j % 2 != 0) or (i %
              2 == 0 and j % 2 == 0))else "0" for j in range(1, i+1)))


def pattern11Concise(n):
    for i in range(1, n+1):
        print(" ".join("1" if (i % 2 == j % 2) else "0" for j in range(1, i+1)))


def pattern12(n):
    for i in range(1, n+1):
        print("".join(map(str, range(1, i + 1))) + " " *
              (2 * (n - i)) + "".join(map(str, range(i, 0, -1))))


def pattern13Verbose(n):
    count = 1
    for i in range(1, n+1):
        for _ in range(1, i+1):
            print(count, end=" ")
            count += 1
        print()


def pattern13Concise(n):
    count = 1
    for i in range(1, n+1):
        print(" ".join(str(count + j) for j in range(i)))
        count += i


def pattern14(n):
    for i in range(1, n+1):
        print("".join(chr(c) for c in range(65, 65+i)))


def pattern15(n):
    for i in range(n, 0, -1):
        print("".join(chr(c) for c in range(65, 65+i)))


def pattern16(n):
    for i in range(1, n+1):
        print(chr(65+i-1)*i)


def pattern17(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "".join(chr(c) for c in range(65, 65+i)) +
              "".join(chr(c) for c in range(64+i-1, 64, -1)))


def pattern18(n):
    for i in range(1, n+1):
        print(" ".join(chr(c) for c in range(65+n-i, 65+n)))


def pattern19(n):
    for i in range(n):
        print("*" * (n-i) + " " * (i*2) + "*" * (n-i))
    for i in range(1, n+1):
        print("*" * i + " " * (2*(n-i)) + "*" * i)


def main():
    # n = int(input("Enter n: "))
    n = 5
    pattern19(n)


if __name__ == "__main__":
    main()
