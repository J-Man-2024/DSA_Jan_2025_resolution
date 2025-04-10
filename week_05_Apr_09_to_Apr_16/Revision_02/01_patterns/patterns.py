
def pattern_01(n):
    for _ in range(n):
        print("".join("*") * n)

def pattern_02(n):
    for i in range(n):
        print("".join("*") * (i + 1))

def pattern_03(n):
    for i in range(1, n + 1):
        print("".join(map(str, range(1, i + 1))))

def pattern_04(n):
    for i in range(1, n + 1):
        print("".join(str(i)) * i)

def pattern_05(n):
    for i in range(n):
        print("".join("*") * (n - i))

def pattern_06(n):
    for i in range(n):
        print("".join(map(str, range(1, n - i + 1))))

def pattern_07(n):
    for i in range(n):
        print("".join(" ") * (n - i - 1) + "".join("*") * (i * 2 + 1))

def pattern_08(n):
    for i in range(n):
        print("".join(" ") * i + "".join("*") * (2 * (n - i) - 1))

def pattern_09(n):
    for i in range(n):
        print("".join(" ") * (n - i - 1) + "".join("*") * (2 * i + 1))
    for i in range(n):
        print("".join(" ") * i + "".join("*") * (2 * (n - i) - 1))

def pattern_10(n):
    for i in range(n * 2 - 1):
        print("".join("*") * (i + 1 if i < n else 2 * n - i - 1))

def pattern_11(n):
    for i in range(n):
        print(" ".join("1" if i % 2 == j % 2 else "0" for j in range(i + 1)))

def pattern_12(n):
    for i in range(1, n + 1):
        print("".join(map(str, range(1, i + 1))) + "".join(" ") * (2 * (n - i)) + "".join(map(str, range(i, 0, -1))))

def pattern_13(n):
    count = 1
    for i in range(1, n + 1):
        print(" ".join(map(str, range(count, count + i))))
        count += i

def pattern_14(n):
    ch = ord('A') 
    for i in range(ch, ch + n):
        print("".join(chr(c) for c in range(ch, i + 1)))

def pattern_15(n):
    ch = ord('A')
    for i in range(n):
        print("".join(chr(c) for c in range(ch, n - i + ch)))
def main():
    n = 5    
    pattern_15(n)
if __name__ == "__main__":
    main()
