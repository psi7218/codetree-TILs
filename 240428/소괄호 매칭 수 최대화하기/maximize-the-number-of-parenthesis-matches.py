n = int(input())

count = 0
arr = []
for _ in range(n):
    check = list(map(str, input()))
    if check.count('(') == len(check):
        count += len(check)
    else:
        arr.append(check)

arr.sort(key=lambda x: (-x.count('('), x.count(')')))
word = []
for ar in arr:
    for a in ar:
        word.append(a)

answer = 0

for wor in word:
    if wor == '(':
        count += 1
    else:
        answer += count

print(answer)