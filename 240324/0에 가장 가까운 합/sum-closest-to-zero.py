n = int(input())
arr = list(map(int, input().split()))
arr.sort()

j = n - 1
answer = 2 * 1e9 + 1
for i in range(n):
    if i < j:
        answer = min(answer, abs(arr[i] + arr[j]))


    while i < j and arr[i] + arr[j] > 0:
        j -= 1
        answer = min(answer, abs(arr[i] + arr[j]))

print(answer)