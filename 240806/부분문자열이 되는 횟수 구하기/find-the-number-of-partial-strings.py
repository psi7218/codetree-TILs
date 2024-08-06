from collections import defaultdict

A = input()
B = input()

order = list(map(int, input().split()))

a_dict = defaultdict(int)
b_dict = defaultdict(int)
for a in A:
    a_dict[a] += 1

for b in B:
    b_dict[b] += 1

flag = False
for key in b_dict:
    if a_dict.get(key):
        if a_dict[key] >= b_dict[key]:
            continue
    
        else:
            flag = True
            break

if flag:
    print(0)
    exit()

answer = 1
for num in order:
    temp = A[num-1]
    a_dict[temp] -= 1
    if a_dict[temp] >= b_dict[temp]:
        answer += 1
    else:
        break

print(answer)