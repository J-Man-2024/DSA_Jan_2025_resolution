
def compute_frequency(s):
    hash_table = [0] * 256
    for char in s:
        hash_table[ord(char)] += 1
    return hash_table

def process_queries(hash_table):
    for _ in range(int(input("How many queries do you want to check? "))):
        c = input("Enter the character you want to check: ").strip()
        print(f"{c} Appears, {hash_table[ord(c)]} times.")

###############
def main():
    s = input("Enter a string: ").strip()
    process_queries(compute_frequency(s))

################
if __name__ == "__main__":
    main()
