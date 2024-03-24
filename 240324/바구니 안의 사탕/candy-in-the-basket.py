n , k = map(int, input().split())
arr = [0] * 1000001
for _ in range(n):
    x, y = map(int, input().split())
    arr[y] = x

max_val = 0
i = 0
sum_val = sum(arr[0:2*k+1])
while i <= 1000000 - 2*k - 1:
    sum_val -= arr[i]
    sum_val += arr[i+2*k+1]
    max_val = max(max_val, sum_val)
    i += 1

print(max_val)