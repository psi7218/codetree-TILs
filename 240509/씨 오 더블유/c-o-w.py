n = int(input())
word = input()

L, R = [0] * n, [0] * n

Ccnt = 0
for i in range(n):
    if word[i] == 'C':
        Ccnt += 1
    L[i] = Ccnt

Wcnt = 0
for j in range(n-1, -1, -1):
    if word[j] == 'W':
        Wcnt += 1
    R[j] = Wcnt

answer = 0

for k in range(n):
    if word[k] == 'O':
        answer += L[k] * R[k]

print(answer)