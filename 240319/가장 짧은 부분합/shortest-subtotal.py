import sys
input = sys.stdin.readline

n, s = map(int, input().split())

num_list = [0] + list(map(int, input().split()))


l = len(num_list)
answer = l
sum = 0
j = 0 
for i in range(l):
    while j <= l - 1 and sum + num_list[j] < s:
        sum += num_list[j]
        j+= 1
    
    answer = min(answer, j - i + 1)
    sum -= num_list[i]


if answer > l :
    print(-1)
else:
    print(answer)