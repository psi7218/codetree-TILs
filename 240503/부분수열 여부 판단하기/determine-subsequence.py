n, m = map(int, input().split())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

j = 0
for i in range(n):
    if arr_A[i] == arr_B[j]:
        j += 1
    
    if j == m:
        break

if j == m:
    print('Yes')
else:
    print('No')