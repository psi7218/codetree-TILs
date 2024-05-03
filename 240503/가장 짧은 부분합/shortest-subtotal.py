n, s = map(int, input().split())

arr = [0] + list(map(int, input().split()))
answer = 1e9
sum1 = 0
j = 1
for i in range(1, n+1):
    while j < n and sum1 < s:
        sum1 += arr[j]
        j += 1

    if sum1 < s:
        break

    answer = min(answer, j - i )

    sum1 -= arr[i]

if answer == 1e9:
    answer = -1

print(answer)