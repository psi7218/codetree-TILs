n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
L, R = [0] * n, [0] * n 

arr.sort()
L[0] = arr[0][1]
for i in range(1, n):
    L[i] = max(arr[i][1], L[i-1])

R[n-1] = arr[n-1][1]
for j in range(n-2,-1, -1):
    R[j] = min(arr[j][1], R[j+1])
    
answer = 0
print(L)
print(R)
for k in range(n):
    _, x2 = arr[k]
    
    if k > 0 and L[k - 1] >= x2:
        continue
  
    if k < n - 1 and R[k + 1] <= x2:
        continue
    
  
    answer += 1
print(answer)