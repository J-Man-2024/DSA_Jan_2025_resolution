from collections import defaultdict
from collections import Counter

arr = [10,5,10,15,10,5]
n = len(arr)

# brute force
# visited = [False] * n
# for i in range(n):
#     if visited[i] == True:
#         continue
#     count = 0
#     for j in range(n):
#         if arr[i] == arr[j]:
#             count += 1
#             visited[j] = True
#     print(f"{arr[i]} appears {count} times.")

# complexities : time = O(n^2) space = O(1)

# optimized approach using hashing
# mp = {}
# for num in arr:
#     mp[num] = mp.get(num, 0) + 1

# for key, value in mp.items():
#     print(f"{key} appears {value} times.")

# complexities : time = O(n) space = O(n)

# alternate apporach 1 using defaultdict
# mp = defaultdict(int)
# for num in arr:
#     mp[num] += 1
# for key, value in mp.items():
#     print(f"{key} appears {value} times.")

# complexities : time = O(n) space = O(n)

# alternate approach 2 using Counter
mp = Counter(arr)
for key, value in mp.items():
    print(f"{key} appears {value} times.")

# complexities : time = O(n) space = O(n)
