import sys 
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

check = [0] * (max(arr) + 1)

answer = 0
j = 0
for i in range(1, n+1):
    while j + 1 <= n and check[arr[j+1]] != 1:
        check[arr[j+1]] += 1
        j += 1

    answer = max(answer, j - i + 1)
    check[arr[i]] -= 1

print(answer)