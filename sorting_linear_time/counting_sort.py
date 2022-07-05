arr = [4, 2, 2, 8, 3, 3, 1]
max_ = max(arr)
size = len(arr)
result = [0] * size
count = [0] * (max_ + 1)

for i in range(size):
    count[arr[i]] += 1

for i in range(1, max_ + 1):
    count[i] += count[i - 1]

i = size - 1
while i >= 0:
    result[count[arr[i]] - 1] = arr[i]
    count[arr[i]] -= 1
    i -= 1

for i in range(size):
    arr[i] = result[i]

print(result)
