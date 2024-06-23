n = int(input())

lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))


answer = []
def func(num, depth):
    if depth == n:
        answer.append(num // 2)
        return

    s, e = lst[depth]
    if s <= num <= e:
        func(2 * num, depth + 1)    


st = [i for i in range(lst[0][0], lst[0][1] + 1)]

for s in st:
    if s % 2 == 0:
        func(s * 2, 1)

answer.sort(key=lambda x : x // 2**n)
print(answer[0] // 2**n)