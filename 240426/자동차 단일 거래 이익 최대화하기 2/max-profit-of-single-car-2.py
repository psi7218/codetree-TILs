n = int(input())

arr = list(map(int, input().split()))

temp = 0
diff = 0
for i in range(n-1,-1,-1):
    if arr[i] >= temp:
        temp = arr[i]
    else:
        diff = max(temp - arr[i], diff)
    
print(diff)