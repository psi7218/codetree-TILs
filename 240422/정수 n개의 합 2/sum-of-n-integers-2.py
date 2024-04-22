n, k = map(int, input().split())
arr = list(map(int, input().split()))

sum1 = [0] * n
sum1[0] = arr[0]
for i in range(1,n):
    sum1[i] = sum1[i-1] + arr[i]

new_arr = [0] + sum1

answer = 0
for i in range(k, n+1):
    answer = max(answer, new_arr[i] - new_arr[i-k])

print(answer)