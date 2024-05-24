from collections import defaultdict

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

answer = 1e9
check = defaultdict(int)
other = defaultdict(int)
for num in range(1, len(num_list)):
    other[num_list[num]] += 1

check[num_list[0]] += 1

j = 1
for i in range(n):
    while j < n and len(check) != m:
        check[num_list[j]] += 1
        other[num_list[j]] -= 1
        if other[num_list[j]] == 0:
            del other[num_list[j]]
        j += 1

    if len(check) == m and len(other) == m:
        answer = min(answer, j - i)

    if check[num_list[i]] == 1:
        del check[num_list[i]]

    else:
        check[num_list[i]] -= 1
    other[num_list[i]] += 1

if answer == 1e9:
    answer = -1

print(answer)