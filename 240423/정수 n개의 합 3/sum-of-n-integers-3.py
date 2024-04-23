import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = [[0] * (n + 1)] + [
    [0] + list(map(int, input().split()))
    for _ in range(n)
]
prefix_sum = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
ans = INT_MIN


# (x1, y1), (x2, y2) 직사각형 구간 내의 원소의 합을 반환합니다.
def get_sum(x1, y1, x2, y2):
    return prefix_sum[x2][y2]     - prefix_sum[x1 - 1][y2] - \
           prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]


# 누적합 배열을 만들어줍니다.
prefix_sum[0][0] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + \
                           prefix_sum[i][j - 1] - \
                           prefix_sum[i - 1][j - 1] + \
                           arr[i][j]

# 모든 직사각형에 대해 합을 찾아
# 그 중 최댓값을 갱신합니다.
for i in range(1, n - k + 2):
    for j in range(1, n - k + 2):
        ans = max(ans, get_sum(i, j, i + k - 1, j + k - 1))

print(ans)