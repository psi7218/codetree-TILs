import sys

input = sys.stdin.readline

n, s = map(int, input().split())

num_list = [0] + list(map(int, input().split()))

l = n + 1
answer = l
sum = 0
j = 0
for i in range(l):
    while j <= l - 1:
        if sum >= s:
            answer = min(answer, j-i)
            sum -= num_list[i]
            break
        sum += num_list[j]
        j += 1

if answer >= l:
    print(-1)
else:
    print(answer)