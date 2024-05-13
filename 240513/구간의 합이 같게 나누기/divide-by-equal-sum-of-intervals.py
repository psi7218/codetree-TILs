n = int(input())
arr = list(map(int, input().split()))

flag = False
if arr == [0] * n:
    flag = True
array = [0] * n
L, R = [0] * n, [0] * n
total = sum(arr)
val = total // 4
a,b,c = val ,val *2, val *3


array[0] = arr[0]
for i in range(1,n):
    array[i] = array[i-1] + arr[i]

acnt = 0
for j in range(n):
    if array[j] == a:
        acnt += 1
    
    L[j] = acnt

ccnt = 0
for k in range(n-2,-1,-1):
    if array[k] == c:
        ccnt += 1
    R[k] = ccnt

answer = 0
for l in range(n):
    if array[l] == b:
        answer += L[l] * R[l]


if not flag:
    print(answer)
else:
    print((n-1) * (n-2) * (n-3) // 6)