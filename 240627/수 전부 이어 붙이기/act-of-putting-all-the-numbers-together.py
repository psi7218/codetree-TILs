n = int(input())
lst = list(map(int, input().split()))
a = ''.join(map(str, lst))

l = len(a)
c, d = l // 5, l % 5
for i in range(c):
    print(a[5*i:5*(i+1)])

print(a[c*5:c*5 + d])