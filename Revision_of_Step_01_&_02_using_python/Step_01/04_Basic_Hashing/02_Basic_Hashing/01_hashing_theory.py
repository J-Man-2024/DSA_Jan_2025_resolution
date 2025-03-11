from collections import defaultdict
from collections import Counter

arr = [1, 3, 2, 1, 3]
charr = "ababac".strip()
nch = len(charr)
n = len(arr)
# visited = [False]*n
# for i in range(n):
#     if visited[i] == True:
#         continue
#     count = 0
#     for j in range(n):
#         if arr[i] == arr[j]:
#             visited[j] = True
#             count += 1
#     print(f"{arr[i]} appears {count} times.")

# visited = []
# for i in range(n):
#     if arr[i] in visited:
#         continue
#     count = 0
#     for j in range(n):
#         if arr[i] == arr[j]:
#             count += 1
#     visited.append(arr[i])
#     print(f"{arr[i]} appears {count} times.")
# hash_table = [0]*13
# for i in range(n):
#     hash_table[arr[i]] += 1

# query = int(input("How many queries you want to check: "))
# for i in range(query):
#     num = int(input("enter the element you want to check: "))
#     print(f"{num} appears {hash_table[num]} times.")

# hash_table = [0]*256
# for ch in charr:
#     hash_table[ord(ch)] += 1

# for _ in range(int(input("Enter amount of query you want to check: "))):
#     ch = input("Enter a character: ").strip()
#     print(f"{ch} appears {hash_table[ord(ch)]} times.")

# mp = {}
# for num in arr:
#     mp[num] = mp.get(num, 0) + 1

# for key, value in mp.items():
#     print(f"{key} appears {value} times.")

# mp = {}
# for ch in charr:
#     mp[ch] = mp.get(ch, 0) + 1
# for key, value in mp.items():
#     print(f"{key} appears {value} times.")

# mp = defaultdict(int)
# for num in arr:
#     mp[num] += 1
# for key, value in mp.items():
#     print(f"{key} appears {value} times.")

# mp = Counter(arr)
# for key, value in mp.items():
#     print(f"{key} appears {value} times.")

# mp = defaultdict(int)
# for ch in charr:
#     mp[ch] += 1
# for key, value in mp.items():
#     print(f"{key} appears {value} times.")

mp = Counter(charr)
for key, value in mp.items():
    print(f"{key} appears {value} times.")
