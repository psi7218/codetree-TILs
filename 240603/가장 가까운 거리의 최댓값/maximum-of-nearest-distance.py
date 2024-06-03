import heapq

n, m = map(int, input().split())
points = list(map(int, input().split()))

INF = int(1e9)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

def dijk(start):
    distance = [INF] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0,start))

    while q:
        dist, now = heapq.heappop(q)

        for node, cost in graph[now]:
            new_cost = dist + cost

            if distance[node] <= new_cost:
                continue
            
            distance[node] = new_cost
            heapq.heappush(q, (new_cost, node))

    return distance
answer = []
for point in points:
    answer.append(dijk(point))

last = 0
for i in range(1,n+1):
    if i in points:
        continue
    
    val = min(answer[0][i], answer[1][i], answer[2][i])
    last = max(last, val)

print(last)