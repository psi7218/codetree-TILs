from collections import defaultdict

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

answer = 1e9
check = defaultdict(int)
check[num_list[0]] += 1
j = 1
for i in range(n):
    while j < n and len(check) != m:
        check[num_list[j]] += 1
        j += 1

    if len(check) == m:
        answer = min(answer, j - i)

    if check[num_list[i]] == 1:
        del check[num_list[i]]
    else:
        check[num_list[i]] -= 1
if answer == 1e9:
    answer = -1

print(answer)