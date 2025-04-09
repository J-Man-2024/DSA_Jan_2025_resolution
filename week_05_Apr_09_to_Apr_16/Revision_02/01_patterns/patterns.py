
def pattern_01(n):
    for _ in range(n):
        print("".join("*") * n)
def pattern_02(n):
    for i in range(1, n + 1):
        print("".join("*") * i)
def pattern_03(n):
    for i in range(1, n + 1):
        print("".join(map(str, range(1, i + 1))))
def pattern_04(n):
    for i in range(1, n + 1):
        print("".join(str(i)) * i)
def pattern_05(n):
    for i in range(1, n + 1):
        print("".join("*") * (n - i + 1))
def pattern_06(n):
    for i in range(n):
        print("".join(map(str, range(1, (n - i + 1)))))
def pattern_07(n):
    for i in range(1, n + 1):
        print("".join(" ") * (n - i) + "".join("*") * (2 * i - 1))
def pattern_08(n):
    for i in range(1, n + 1):
        print("".join(" ") * (i - 1) + "".join("*") * (2 * (n - i) + 1))
def pattern_09(n):
    for i in range(1, n + 1):
        print("".join(" ") * (n - i) + "".join("*") * (2 * i - 1))
    for i in range(1, n + 1):
        print("".join(" ") * (i - 1) + "".join("*") * (2 * (n - i) + 1))
def pattern_10(n):
    for i in range(1, n * 2):
        print("".join("*") * (i if i < n else (n * 2 - i)))
def pattern_11(n):
    for i in range(n):
        print(" ".join("1" if i % 2 == j % 2 else "0" for j in range(i + 1)))   
def main():
    n = 5    
    pattern_11(n)
if __name__ == "__main__":
    main()
