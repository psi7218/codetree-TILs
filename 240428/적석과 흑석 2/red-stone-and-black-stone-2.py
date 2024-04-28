c, n = map(int, input().split())

cball = []
tball = []
answer = 0
for _ in range(c):
    cball.append(int(input()))

for _ in range(n):
    tball.append(list(map(int, input().split())))



cball.sort(reverse=True)

tball.sort(key=lambda x : -x[0])


idx = 0
for start, end in tball:

    while idx < c:
        if start <= cball[idx] <= end:
            answer += 1
            idx += 1
            break
        else:
            idx += 1

print(answer)