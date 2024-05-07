n = int(input())
arr = [0,0] + list(map(int, input().split())) + [0,0]

L, R = [0] * (n+4), [0] * (n+4)
max_val = 0
for i in range(2, n+4):
    max_val = max(max_val, arr[i-2])
    L[i-2] = max_val


max_val = 0
for j in range(n+1, -1,-1):
      max_val = max(max_val, arr[j + 2])
      R[j+2] = max_val

answer = 0
for k in range(4, n):

    answer = max(answer, L[k-2] + R[k+2] + arr[k])


print(answer)