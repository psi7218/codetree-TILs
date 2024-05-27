import heapq

n, m = map(int, input().split())
k = int(input())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())

    graph[x].append((y,z))
    graph[y].append((x,z))

def func(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        for next in graph[now]:
            next_node = next[0]
            next_cost = next[1]

            new_cost = dist + next_cost

            if new_cost >= distance[next_node]:
                continue
            
            distance[next_node] = new_cost
            heapq.heappush(q, (new_cost, next_node))

func(k)
for i in range(1,n+1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])