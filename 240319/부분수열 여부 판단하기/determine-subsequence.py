import sys
input = sys.stdin.readline

n, m  = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))


def twopoint():
    i = 1 
    for j in range(1,m+1):
        while i <= n  and a[i] != b[j]:
            i += 1

        if i == n + 1:
            return False
        
        else :
            i += 1
    
    return True


if twopoint():
    print("Yes")
else:
    print("No")