import sys
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())

uf = [i for i in range(n+1)]


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


answer = 0
for _ in range(m):
    num = int(input())
    val = find(num)

    if val == 0:
        break
    
    uf[val] = find(val -1)

print(answer)