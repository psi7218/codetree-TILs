import heapq
n = int(input())

q = list(map(int, input().split()))
answer = 0

while len(q) >= 2:
    temp = 0
    for _ in range(2):
        temp += heapq.heappop(q)
    answer += temp
    heapq.heappush(q, temp)

print(answer)