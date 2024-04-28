n = int(input())

arr = []
for _ in range(n):
    check = list(map(str, input()))
    arr.append(check)


arr.sort(key=lambda x: (-x.count('('), x.count(')')))
word = []
for ar in arr:
    for a in ar:
        word.append(a)

answer = 0
count = 0
for wor in word:
    if wor == '(':
        count += 1
    else:
        answer += count

print(answer)