def compute_frequency(arr):
    hash_table = [0]*13
    for num in arr:
        hash_table[num] += 1
    return hash_table
def process_queries(hash_table):
    for _ in range(int(input("How many queries do you want to check? "))):
        num = int(input("Enter the element you want to check: "))
        print(f"{num} Appears, {hash_table[num]} times.")
############
def main():
    #n = int(input("Enter n: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    process_queries(compute_frequency(arr))    
############
if __name__ == "__main__":
    main()

