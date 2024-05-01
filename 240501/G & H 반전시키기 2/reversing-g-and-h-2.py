n = int(input())

first = input()
second = input()
start = []
end = []

for i in range(n):
    if first[i] == 'G':
        start.append(0)
    else:
        start.append(1)

    if second[i] == 'G':
        end.append(0)
    else:
        end.append(1)

answer = 0
for j in range(n-1, -1, -1):
    if start[j] != end[j]:
        for k in range(j,-1,-1):
            start[k] ^= 1

        answer += 1

print(answer)