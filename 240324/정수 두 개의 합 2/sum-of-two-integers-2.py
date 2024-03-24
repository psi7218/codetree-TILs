n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

cnt = 0
j = 1
for i in range(n):
    while j < n and arr[i] + arr[j] <= k:
        cnt += 1
        j += 1
    
print(cnt)