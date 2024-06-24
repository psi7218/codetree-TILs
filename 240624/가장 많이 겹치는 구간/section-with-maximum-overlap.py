n = int(input())
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a,b])
lst.sort(key=lambda x : x[1])

mval = lst[-1][1]

check = [0] * (mval + 1)

for start, end in lst:
    check[start] += 1
    check[end] -= 1

for i in range(1, mval+1):
    check[i] = check[i-1] + check[i]
print(max(check))