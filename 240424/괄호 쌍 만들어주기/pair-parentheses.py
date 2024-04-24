arr = [0] + list(map(str, input()))
n = len(arr)

open = [0] * (n)
close = [0] * (n)

for idx in range(1,n-1):
    if arr[idx] == "(" and arr[idx+1] == "(":
        open[idx] = open[idx-1] + 1
    else:
        open[idx] = open[idx-1]

    if arr[idx] == ")" and arr[idx+1] == ")":
        close[idx] = 1

answer = 0

for i in range(n):
    answer += open[i] * close[i]

print(answer)