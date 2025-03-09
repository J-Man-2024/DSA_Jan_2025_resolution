from collections import defaultdict
from collections import Counter

arr = [10, 5, 10, 15, 10, 5]
# visited = []
# for i in range(len(arr)):
#     if arr[i] in visited:
#         continue
#     count = 0
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             count += 1
#     print(f"{arr[i]} appears {count} times.")
#     visited.append(arr[i])
# visited = [False]*len(arr)
# for i in range(len(arr)):
#     if visited[i] == True:
#         continue
#     count = 0
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             visited[j] = True
#             count += 1
#     print(f"{arr[i]} appears : {count} times.")
# visited = set()
# for i in range(len(arr)):
#     if arr[i] in visited:
#         continue
#     count = 0
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             count += 1
#     print(f"{arr[i]} appears {count} times.")
#     visited.add(arr[i])
# mp = {}
# for num in arr:
#     mp[num] = mp.get(num, 0) + 1
# for key, value in mp.items():
#     print(f"{key} appears {value} times.")
# mp = defaultdict(int)
# for num in arr:
#     mp[num] += 1
# for key, value in mp.items():
#     print(f"{key} appears {value} times.")
mp = Counter(arr)
for key, value in mp.items():
    print(f"{key} appears {value} times.")
