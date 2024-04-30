n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(1,n-1 ):
	if arr[i-1] == 0:
		arr[i-1] = 1
		if arr[i] == 1:
			arr[i] = 0
		else:
			arr[i] = 1
		if arr[i+1] == 1:
			arr[i+1] = 0
		else:
			arr[i+1] = 1

		answer += 1

if arr[-1] and arr[-2] and sum(arr[:n-2]) == n - 2:
	print(answer)
else:
	print(-1)