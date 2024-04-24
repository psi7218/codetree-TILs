from collections import defaultdict

n, k = map(int, input().split())

check = dict()

arr = []
for _ in range(n):
    arr.append(int(input()))

answer = -1
for idx in range(n):
    if arr[idx] in check:
        if idx - check[arr[idx]] <= k:
            answer = max(answer, arr[idx])
    else:
        check[arr[idx]] = idx


print(answer)