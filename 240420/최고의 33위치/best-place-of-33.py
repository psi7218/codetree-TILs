n = int(input())

arr = []
answer = 0
for _ in range(n):
    arr.append(list(map(int, input().split())))

def func(x,y):
    cnt = 0
    for a in range(x,x+3):
        for b in range(y,y+3):
            if arr[a][b] == 1:
                cnt += 1
    return cnt

for i in range(n-2):
    for j in range(n-2):
        answer = max(answer, func(i,j))


print(answer)