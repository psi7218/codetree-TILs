n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])

answer = 0
time = 0
idx = 0
while idx < n:
    start, end = arr[idx]
    if start >= time:
        answer += 1
        time = end

    idx += 1

print(answer)