n = int(input())

meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append([s,e])

meeting.sort(key=lambda x: (x[1], [0]))

answer = 0
temp = 0
for start, end in meeting:
    if start >= temp:
        temp = end
    else:
        answer += 1

print(answer)