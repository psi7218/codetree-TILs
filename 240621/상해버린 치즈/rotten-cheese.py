n, m, d, s = map(int, input().split())

cheese_eat = [[] for _ in range(m + 1)]
record = [[] for _ in range(n + 1)]


for _ in range(d):
    a, b, c = map(int, input().split())
    record[a].append((b,c))
    cheese_eat[b].append(a)

timing = [0] * (n + 1)
for _ in range(s):
    a, b = map(int, input().split())
    timing[a] = b

check = [0] * (m + 1)
for idx in range(1, n + 1):
    for m, t in record[idx]:
        if t < timing[idx]:
            check[m] += 1

last = set()
for ix in range(1, len(check)):
    if check[ix] == s:
        last.add(ix)

answer = 0
for la in last:
    answer = max(answer, len(cheese_eat[la]))

print(answer)