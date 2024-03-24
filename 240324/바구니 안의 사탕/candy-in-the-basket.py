n, k = tuple(map(int, input().split()))
candies = [(-1, -1)]
for _ in range(n):
    cnt, x = tuple(map(int, input().split()))
    candies.append((x, cnt))

def get_pos_of_candy(candy_idx):
    x, _ = candies[candy_idx]
    return x


def get_num_of_candy(candy_idx):
    _, cnt = candies[candy_idx]
    return cnt

candies.sort()


ans = 0
total_nums = 0
j = 0
for i in range(1, n + 1):
    while j + 1 <= n and candies[j + 1][0] - candies[i][0] <= 2 * k:
        total_nums += candies[j + 1][1]
        j += 1
 
    ans = max(ans, total_nums)
    total_nums -= candies[i][1]

print(ans)