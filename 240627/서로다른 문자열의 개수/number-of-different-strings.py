n = int(input())


def factorial(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total

val = factorial(2*n) / (factorial(n+1) * factorial(n))
print(int(val))