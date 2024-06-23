n = int(input())
line = list(map(int, input()))
answer = 0
temp = - 1
for i in range(n):
    if line[i] == 1:
        if temp == -1:
            answer = i
            temp = i
        else:
            answer = max(answer, (i - temp) // 2)
            temp = i

    elif i == n - 1 and line[i] == 0:
        answer = max(answer, (i - temp))

print(answer)