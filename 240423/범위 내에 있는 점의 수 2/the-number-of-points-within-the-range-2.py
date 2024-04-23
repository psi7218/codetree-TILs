n, q = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * 1000001
for num in arr:
    prefix[num] = 1

for i in range(1, 1000001):
    prefix[i] = prefix[i-1] + prefix[i]

for _ in range(q):
    x, y = map(int, input().split())
    val = prefix[y] - prefix[x-1]
    print(val)