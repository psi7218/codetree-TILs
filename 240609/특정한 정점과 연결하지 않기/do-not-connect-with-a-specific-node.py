import sys
input = sys.stdin.readline

n, m = map(int, input().split())

uf = [i for i in range(n+1)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    uf[b] = a

chart = [[1,i] for i in range(n + 1)]
graph = [sorted(list(map(int, input().split()))) for _ in range(m)]
graph.sort(key = lambda x : x[0])

s, t, cnt = map(int, input().split())

phase = [set() for j in range(n+1)]

for start, end in graph:
    union(start, end)
    idx = find(start)
    phase[idx].add(end)


for ix in range(len(phase)):
    chart[ix] = [len(phase[ix]) + 1, ix]
chart.sort(key = lambda x : -x[0])
answer = len(phase[s]) + 1

for count, index in chart:
    if cnt == 0:
        break
    if index == s or index == 0:
        continue

    if t in phase[index]:
        continue
    
    else:
        if find(t) != find(index) and find(s) != find(index):
            answer += count
            cnt -= 1

# print(phase)
# print(chart)
print(answer)