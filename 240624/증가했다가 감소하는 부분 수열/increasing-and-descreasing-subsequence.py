n = int(input())
# (감소, 증가)
ar = list(map(int, input().split()))
answer = 0
def func(k):
    high = [1] * (k + 1)
    low = [1] * (n - k - 1)
    harr = ar[:k + 1]
    larr = ar[k+1:]
    for i in range(1, len(harr)):
        for j in range(i):
            if harr[j] < harr[i]:
                high[i] = max(high[i], high[j] + 1)

    for i in range(1, len(larr)):
        if larr[i] >= ar[k]:
            continue
        for j in range(i):
            if larr[j] > larr[i]:
                low[i] = max(low[i], low[j] + 1)

    if high and low:
        return max(high) + max(low)

    else:
        if high:
            return max(high)
        else:
            return max(low)


for k in range(n):
    answer = max(answer, func(k))

print(answer)