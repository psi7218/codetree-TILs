n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
answer = []
i = 0
j = 1
while i < j and i < n:
    while j < n and arr[j] - arr[i] <= k:
        j += 1
    
    answer.append(j-i)
    i = j
    j += 1

answer.sort()
ans = 0
for _ in range(2):
    ans += answer.pop()

print(ans)