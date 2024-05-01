n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

answer = 0
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if arr[i][j] == 1:
            answer += 1
            for a in range(i,-1,-1):
                for b in range(j,-1,-1):
                    arr[a][b] ^= 1

            

print(answer)