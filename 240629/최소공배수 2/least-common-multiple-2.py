a, b = map(int, input().split())

val = a if a <= b else b


total = 1
temp = 2
while temp <= val:
    if a % temp == 0 and b % temp == 0:
        total *= temp
        a = a // temp
        b = b // temp
    else:
        temp += 1

print(total * a * b)