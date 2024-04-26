n = int(input())
m = 0
arr = []
val = 2e9 + 5
for _ in range(n):
    a, b = map(int, input().split())
    m += a
    for _ in range(a):
        arr.append(b)

answer = 0
arr.sort()
for i in range(m//2):
    val = arr[i] + arr[-1-i]
    answer = max(answer, val)

print(answer)