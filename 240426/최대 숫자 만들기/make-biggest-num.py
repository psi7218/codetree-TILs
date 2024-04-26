from functools import cmp_to_key

n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

def compare(x,y):
    if x + y > y + x:
        return -1
    elif x + y< y + x:
        return 1
    else:
        return 0

arr.sort(key=cmp_to_key(compare))
for num in arr:
    print(num, end="")