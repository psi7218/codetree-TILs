n = int(input())
dp = [[1, 1] for _ in range(n)]
high = [1] * n
low = [1] * n
# (감소, 증가)
ar = list(map(int, input().split()))
answer = 0
for i in range(1, n):
    for j in range(i):
        if ar[j] < ar[i]:
            high[i] = max(high[i], high[j] + 1)

        elif ar[j] > ar[i]:
            low[i] = max(low[i], low[j] + 1)

# print(high)
# print(low)

for k in range(1, n-1):
    if ar[k-1] < ar[k] > ar[k+1]:
        temp = ar[k+1:n]
        tmp = [1] * len(temp)
        for s in range(1, len(temp)):
            # if temp[s] >= ar[k]:
            #     break
            for t in range(s):
                if temp[t] > temp[s]:
                    tmp[s] = max(tmp[s], tmp[t] + 1)

        answer = max(answer, high[k] + max(tmp))

answer = max(answer, max(low))
print(answer)