n, m = map(int, input().split())

def func(depth, lst):
    if len(lst) == m:
        print(*lst)
        return
    for i in range(1,n+1):
        func(depth + 1, lst + [i])


func(0,[])