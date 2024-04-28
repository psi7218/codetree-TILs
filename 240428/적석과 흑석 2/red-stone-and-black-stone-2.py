from sortedcontainers import SortedSet

# 변수 선언 및 입력:
c, n = tuple(map(int, input().split()))
red_stones = [
    int(input())
    for _ in range(c)
]

black_stones = []
for _ in range(n):
    a, b = tuple(map(int, input().split()))
    black_stones.append((b, a))

# 빨간 돌을 전부 treeset에 넣어줍니다.
# 추후 검은색 돌 기준으로
# Aj보다 같거나 큰 최소 Ti값을 빠르게 찾기 위해
# treeset을 이용합니다.
red_s = SortedSet(red_stones)

# b 기준 오름차순 정렬을 진행합니다.
black_stones.sort()

# b가 작은 돌부터 보며
# a보다 같거나 큰 최소 Ti를 찾습니다.
# 이 값이 만약 b보다 같거나 작다면
# 이 돌을 선택하는 것이 최선입니다.
ans = 0
print(black_stones)
print(red_s)
for b, a in black_stones:
    # a보다 같거나 큰 값이 있다면
    idx = red_s.bisect_left(a)
    if idx != len(red_s):
        # 최소 Ti를 선택합니다.
        ti = red_s[idx]
        # Ti가 b보다 같거나 작다면
        # 매칭을 진행합니다.
        if ti <= b:
            ans += 1
            red_s.remove(ti)

print(ans)