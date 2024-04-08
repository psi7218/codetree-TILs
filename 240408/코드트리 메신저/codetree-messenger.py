from collections import defaultdict

n, q = map(int, input().split())
first = list(map(int, input().split()))

node = [0] + first[1:n+1]
depth_list = [(0,True)]
for a in range(n+1, len(first)):
    depth_list.append([first[a], True])


tree = defaultdict(set)
for idx in range(1, len(node)):
    tree[node[idx]].add(idx)


def func(num,depth):
    for node in tree[num]:
        if depth_list[node][1]:
            if depth_list[node][0] >= depth:
                link.append(node)
                func(node, depth + 1)
            else:
                func(node, depth + 1)


# print(node)
# print(tree)
# print(depth_list)
# print('------------------')
for _ in range(q-1):
    command = list(map(int, input().split()))
    link = []   # 연결할 수 있는 노드 리스트
    if command[0] == 500:
        func(command[1], 1)
        print(len(link))

    elif command[0] == 300:
        nde, power = command[1], command[2]
        depth_list[nde][0] = power

    elif command[0] == 200:
        depth_list[command[1]][1] = not depth_list[command[1]][1]

    elif command[0] == 400:
        x, y = command[1], command[2]
        tree[node[x]].remove(x)
        tree[node[y]].add(x)

        tree[node[y]].remove(y)
        tree[node[x]].add(y)
        node[x], node[y] = node[y], node[x]
        # depth_list[x], depth_list[y] = depth_list[y], depth_list[x]

    # print(node)
    # print(tree)
    # print(depth_list)
    # print('------------------')