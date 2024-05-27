import heapq

n, m = map(int, input().split())

INF = int(1e9)
distance = [INF] * ( n+1 )

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())

    graph[x].append((y,z))
    graph[y].append((x,z))

start, end = map(int, input().split())
path = [0] * (n+1)

def func(st):
    q = []
    heapq.heappush(q, (0,st))
    distance[st] = 0

    while q:
        dist, now = heapq.heappop(q)

        for next_node, cost in graph[now]:
            new_cost = cost + dist

            if distance[next_node] <= new_cost:
                continue
            
            distance[next_node] = new_cost
            path[next_node] = now
            heapq.heappush(q, (new_cost, next_node))

func(start)
a = end
answer = [a]
while a != start:
    a = path[a]
    answer.append(a)

print(distance[end])
print(*answer[::-1])