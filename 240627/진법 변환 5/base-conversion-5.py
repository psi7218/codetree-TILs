num, n = map(int, input().split())

if n == 2:
    print(bin(num)[2:])
elif n == 8:
    print(oct(num)[2:])
else:
    print(hex(num)[2:])