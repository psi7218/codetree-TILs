n, q = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * 1000002
for num in arr:
    prefix[num+1] = 1

for i in range(2, 1000001):
    prefix[i] = prefix[i-1] + prefix[i]

for _ in range(q):
    x, y = map(int, input().split())
    val = prefix[y+1] - prefix[x]
    print(val)