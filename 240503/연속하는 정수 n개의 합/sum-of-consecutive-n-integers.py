n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

answer = 0
j = 1
sum1 = 0
for i in range(1, n+1):
    while j < n + 1 and sum1 < m:
        sum1 += arr[j]
        j += 1

    if sum1 == m:
        answer += 1
        
    
    sum1 -= arr[i]
    if sum1 == m:
        answer += 1

print(answer)