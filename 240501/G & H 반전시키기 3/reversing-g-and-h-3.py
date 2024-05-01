n = int(input())

first = input()
second = input()

start = []
end = []

for i in range(n):
    if first[i] == 'G':
        start.append(0)
    else:
        start.append(1)
    
    if second[i] == 'G':
        end.append(0)
    else:
        end.append(1)

answer = 0
idx = 0
while idx < n:
    j = 0
    if start[idx] != end[idx]:
        for num in range(1,4):
            if idx + num <= n -1 :
                if start[idx+ num] != end[idx + num]:
                    j = num
                else:
                    break
    else:
        idx += 1
        continue

    for x in range(idx, idx + j + 1):
        start[x] ^= 1
    answer += 1
    idx = j + 1

print(answer)