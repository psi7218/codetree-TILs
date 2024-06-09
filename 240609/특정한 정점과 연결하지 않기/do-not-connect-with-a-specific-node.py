import sys
input = sys.stdin.readline

n, m = map(int, input().split())

uf = [i for i in range(n+1)]
visited = [False] * (n + 1)
size = [1] * (n + 1)
def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    if a != b:
        uf[a] = b 
        size[b] += size[a]

for _ in range(m):
    c, d = map(int, input().split())
    union(c, d)

s, t, cnt = map(int, input().split())

start = find(s)
end = find(t)
num_list = []
for i in range(1, n + 1):
    idx = find(i)

    if idx == start or idx == end:
        continue

    if visited[idx]:
        continue
    
    visited[idx] = True
    num_list.append(size[idx])

answer = size[start]
num_list.sort(reverse=True)

for z in range(min(cnt, len(num_list))):
    answer += num_list[z]

print(answer)