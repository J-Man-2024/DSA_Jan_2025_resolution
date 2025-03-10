from collections import defaultdict

arr = [10, 5, 10, 15, 10, 5]
n = len(arr)
# maxFreq, minFreq = 0, n
# maxEle = minEle = None

# for i in range(n):
#     count = 0
#     for j in range(n):
#         if arr[i] == arr[j]:
#             count += 1
#     if count > maxFreq:
#         maxFreq = count
#         maxEle = arr[i]
#     if count < minFreq:
#         minFreq = count
#         minEle = arr[i]
# print(f"maxElement: {maxEle} appears {maxFreq} \nminElement: {minEle} appears {minFreq}")

freq = defaultdict(int)
#Count frequencies
for num in arr:
    freq[num] += 1

#find max and min freq elements
max_element = max(freq, key = lambda x: freq[x])
min_element = min(freq, key = lambda x: freq[x])

print(f"{max_element, min_element}")
