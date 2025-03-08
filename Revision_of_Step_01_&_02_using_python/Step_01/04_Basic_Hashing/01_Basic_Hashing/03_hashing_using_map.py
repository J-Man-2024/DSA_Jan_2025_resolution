from collections import defaultdict

def pre_computation(arr):
    mp = defaultdict(int)
    for num in arr:
        mp[num] += 1
    return mp

def process_queries(mp):
    for _ in range(int(input("How many queries do you want to check? "))):
        num = int(input("Enter the elements you want to check: "))
        print(f"{num} Appears, {mp[num]} times.")

#############
def main():
    arr = list(map(int, input("Enter array elements: ").split()))
    process_queries(pre_computation(arr))

############
if __name__ == "__main__":
    main()
