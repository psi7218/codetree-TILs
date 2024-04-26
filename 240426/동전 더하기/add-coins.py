n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

cnt = 0 

idx = 0

while k != 0:
    cnt += k // coin[idx]
    k = k % coin[idx]
    idx += 1

print(cnt)