from collections import defaultdict, Counter

arr = [10,5,10,15,10,5]
n = len(arr)

#brute force using loops
# visited = [False] * n
# maxFreq, minFreq = 0, n
# minEle = maxEle = None

# for i in range(n):
#     if visited[i] == True:
#         continue
#     count = 0
#     for j in range(n):
#         if arr[i] == arr[j]:
#             count += 1
#             visited[j] = True
#     if maxFreq < count:
#         maxFreq = count
#         maxEle = arr[i]
#     if minFreq > count:
#         minFreq = count
#         minEle = arr[i]
# print(f"Min freq element : {minEle} appears {minFreq} times.\nMax freq element : {maxEle} appears {maxFreq} times.")

# complexities : time = O(n^2) O(1)

#optimized using map

# mp = {}
maxFreq, minFreq = 0, n
maxEle = minEle = None

# for num in arr:
#     mp[num] = mp.get(num, 0) + 1

# for key, value in mp.items():
#     if maxFreq < value:
#         maxFreq = value
#         maxEle = key
#     if minFreq > value:
#         minFreq = value
#         minEle = key
# print(f"min {minEle} : {minFreq}\nmax {maxEle} : {maxFreq}")

# mp = defaultdict(int)
# for num in arr:
#     mp[num] += 1
# for key, value in mp.items():
#     if maxFreq < value:
#         maxFreq = value
#         maxEle = key
#     if minFreq > value:
#         minFreq = value
#         minEle = key
# print(f"{minEle} : {minFreq}\n{maxEle} : {maxFreq}")

mp = Counter(arr)
for key, value in mp.items():
    if maxFreq < value:
        maxFreq = value
        maxEle = key
    if minFreq > value:
        minFreq = value
        minEle = key
print(f"{minEle} : {minFreq}\n{maxEle} : {maxFreq}")
