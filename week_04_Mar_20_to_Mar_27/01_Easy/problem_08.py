# Problem : Linear search.

def linear_search(arr, num):
    found = False
    index = -1
    for i in range(len(arr)):
        if arr[i] == num:
            found = True
            index = i
    if found:
        print(f"{num} is in index {index}.")
    else:
        print(f"{num} is not in the array.")

def main():
    arr = [1, 2, 3, 4, 5]
    num = 3
    linear_search(arr, num)
if __name__ == "__main__":
    main()
