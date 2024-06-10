# 변수 선언 및 입력:
n = int(input())
m = int(input())

# 번호별 그룹을 관리합니다.
# uf[i] : i번 보다 작거나 같은 위치 중에 값이 들어갈 수 있는 최대 위치를 의미합니다.
uf = [0] * (n + 1)

# 초기 uf 값을 설정합니다.
for i in range(1, n + 1):
    uf[i] = i


# x의 대표 번호를 찾아줍니다.
def find(x):
    # x가 루트 노드라면 x값을 반환합니다.
    if uf[x] == x:
        return x
    # x가 루트 노드가 아니라면
    # x의 부모인 uf[x]에서 탐색을 더 진행한 뒤
    # 찾아낸 루트 노드를 uf[x]에 넣어줌과 동시에
    # 해당 노드값을 반환합니다.
    uf[x] = find(uf[x])
    return uf[x]


# m개의 정보를 입력받습니다. x번 보다 작거나 같은 위치에 값이 들어갈 수 있는지 확인합니다.
ans = m
for i in range(1, m + 1):
    x = int(input())
   
    # x번보다 작거나 같은 위치 중에 값이 들어갈 수 있는 최대 위치로 이동합니다.
    X = find(x)
    if X == 0:
        # 그런 값이 없다면 공을 넣을 수 없습니다.
        ans = i - 1
        break

    # X번보다 작은 위치 중에 값이 들어갈 수 있는 최대 위치로 이동합니다.
    Y = find(X - 1)
    uf[X] = Y

print(ans)