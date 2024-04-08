from collections import deque
from collections import defaultdict

l, q = map(int, input().split())
belt = deque([defaultdict(int) for _ in range(l)])
man = [defaultdict(int) for _ in range(l)]
seatisfull = set() ## 현재 사람이 있는 좌석 인덱스 조합
time = 0

menu_cnt = 0
for _ in range(q):
    cmd = list(map(str, input().split()))
    # t초에 x위치에 name이름을 부착한 초밥을 1개 만듬(주방장)

    now1 = (int(cmd[1]) - time) % l
    for _ in range(now1):
        belt.appendleft(belt.pop())

    time = int(cmd[1])
    delete_list = []

    if int(cmd[0]) == 100:
        t, x, name = int(cmd[1]), int(cmd[2]), cmd[3]
        # now2 = (t - time) % l

        belt[x][name] += 1
        menu_cnt += 1

    # name이라는 손님이 t초에 x위치에 앉아서 n개의 초밥을 먹을때까지 기다림(손님)
    elif int(cmd[0]) == 200:
        delete_list = []
        t, x, name, n = int(cmd[1]), int(cmd[2]), cmd[3], int(cmd[4])
        man[x][name] += n
        seatisfull.add(x)

    # 사진촬용 남아있는 사람수와 초밥의 수를 출력
    else:
        t = int(cmd[1])

    for seat in seatisfull:
        for key in man[seat]:
            if belt[seat][key]:
                count = belt[seat][key]
                man[seat][key] -= count
                menu_cnt -= count
                belt[seat][key] -= count
                if man[seat][key] <= 0:
                    delete_list.append((seat, key))
            else:
                del belt[seat][key]

    for seat1, name1 in delete_list:
        del man[seat1][name1]
        del belt[seat1][name1]
        seatisfull.remove(seat1)

    # print(f'seatisfull :{seatisfull}, time : {t}')
    # print(f'belt : ${belt}')
    # print(f'man : ${man}')
    # print('------------------------------')
    if int(cmd[0]) == 300:
        print(len(seatisfull), menu_cnt)