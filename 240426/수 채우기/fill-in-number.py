n = int(input())



val = n // 5
rest = n % 5

def check(num):
    global val, rest
    if num < 5:
        if num == 1 or num == 3:
            return -1
        if num == 2:
            return 1
        if num == 4:
            return 2

    answer = 0
    if rest % 2 == 1:
        val -= 1

    answer += val
    
    num -= val * 5

    answer += (num // 2)
    return answer 

print(check(n))