n, m = map(int, input().split())
uf = [i for i in range(n+1)]


def find(x):
    if uf[x] == x:
        return x
    root = find(uf[x])
    uf[x] = root
    return root


def union(x, y):
    a = find(x)
    b = find(y)

    uf[b] = a


for _ in range(m):
    cmd, s, t = map(int, input().split())
    if cmd == 0:
        union(s, t)

    else:
        val = find(s)
        val1 = find(t)

        if val == val1:
            print(1)
        else:
            print(0)