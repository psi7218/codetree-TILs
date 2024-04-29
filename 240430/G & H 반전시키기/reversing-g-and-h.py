n = int(input())

first = input()
second = input()

bit = []

for i in range(n):
    if first[i] == second[i]:
        bit.append(1)
    else:
        bit.append(0)


temp = bit[0]
answer = 0
for j in range(1,n):
    if bit[j] != temp:
        answer += 1
        temp = bit[j]

print(answer // 2 + answer % 2)