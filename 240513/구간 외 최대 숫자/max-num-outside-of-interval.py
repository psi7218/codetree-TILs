n , q = map(int, input().split())
arr = list(map(int, input().split()))

L, R = [0] * n , [0] * n 
L[0] = arr[0]
for i in range(1,n):
    L[i] = max(L[i-1], arr[i])

R[n-1] = arr[n-1]
for j in range(n-2,-1,-1):
    R[j] = max(R[j+1], arr[j])


for _ in range(q):
    l, r = map(int, input().split())

    left = L[l-2]
    right = R[r]

    answer = max(left, right)
    print(answer)