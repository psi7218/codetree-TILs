n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [[0] * n for _ in range(n)]

cnt = 0
for i in range(n):
    prefix[i][i] = arr[i]
    if prefix[i][i] == k:
        cnt += 1

for a in range(n):
    for b in range(a+1, n):
        prefix[a][b] = prefix[a][b-1] + arr[b]
        if prefix[a][b] == k:
            cnt += 1

print(cnt)