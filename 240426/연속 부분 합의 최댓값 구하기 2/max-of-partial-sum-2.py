n = int(input())
arr = list(map(int, input().split()))

max_val = -1e9

idx = 0
temp = 0

while idx < n:
    temp = max(temp + arr[idx], arr[idx])
    max_val = max(max_val, temp)

    idx += 1

print(max_val)