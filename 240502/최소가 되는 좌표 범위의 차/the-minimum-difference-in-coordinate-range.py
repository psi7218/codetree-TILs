n, d = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x : x[1])

start = 0
end = 1
answer = 1e9 

while end < n:
    temp_x , temp_y = arr[start][0], arr[start][1]
    now_x, now_y = arr[end][0], arr[end][1]
    if now_y - temp_y >= d:
        answer = min(answer, abs(now_x - temp_x))
        if end - start >= 2:
            start += 1
        else:
            end += 1
    else:
        end += 1

print(answer)