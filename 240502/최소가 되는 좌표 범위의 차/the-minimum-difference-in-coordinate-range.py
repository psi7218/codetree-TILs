import sys
from sortedcontainers import SortedSet

n, d = tuple(map(int, input().split()))
point = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

point = [(0, 0)] + sorted(point)

point_count = SortedSet()


def get_min():
    if not point_count:
        return 0
    return point_count[0][0]


def get_max():
    if not point_count:
        return 0
    return point_count[-1][0]


ans = sys.maxsize


j = 0
for i in range(1, n + 1):
    while j + 1 <= n and get_max() - get_min() < d:
        point_count.add((point[j + 1][1], point[j + 1][0]))
        j += 1

    if get_max() - get_min() < d:
        break
    ans = min(ans, point[j][0] - point[i][0])

    point_count.remove((point[i][1], point[i][0]))


if ans == sys.maxsize:
    print(-1)
else:
    print(ans)