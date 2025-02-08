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


def main():
    # n = int(input("Enter n: "))
    n = 5
    pattern06Concise(n)


if __name__ == "__main__":
    main()
