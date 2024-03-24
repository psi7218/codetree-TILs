n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

cnt = 0
j = n - 1
for i in range(n):
    while j != 1 and arr[i] + arr[j] > k:
        j -= 1
    
    if j <= i:
        break
    
    cnt += j - i 
    
    
print(cnt)