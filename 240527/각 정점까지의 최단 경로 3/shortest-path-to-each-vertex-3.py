import heapq

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

INF = int(1e9)
dis = [INF] * (n+1)
dis[1] = 0

def func():
    q = []
    heapq.heappush(q,(0,1))

    while q:
        dist, now = heapq.heappop(q)

        if dis[now] < dist:
            continue
        
        for next in arr[now]:
            new_node = next[0]
            new_dist = next[1]

            if dist + new_dist >= dis[new_node]:
                continue
            
            dis[new_node] = dist + new_dist
            heapq.heappush(q, (dist + new_dist, new_node))

for _ in range(m):
    x, y, z = map(int, input().split())
    arr[x].append((y,z))

func()
for i in range(2,n+1):
    if dis[i] == INF:
        print(-1)
    else:
        print(dis[i])