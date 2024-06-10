n = int(input())
m = int(input())

uf = [i for i in range(n+1)]


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


answer = m
for i in range(1,m + 1):
    num = int(input())
    val = find(num)

    if val == 0:
        answer = i - 1
        break

    uf[val] = find(val -1)

print(answer)