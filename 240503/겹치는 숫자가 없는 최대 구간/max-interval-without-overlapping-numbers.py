n = int(input())
arr = [0] + list(map(int, input().split()))
counting = [0] * (max(arr) + 1)

answer = 0
j = 1
for i in range(1,n + 1):
    while j < n and counting[arr[j]] == 0:
        counting[arr[j]] += 1
        j += 1

    answer = max(answer, j - i)
    counting[arr[i]] -= 1

print(answer)