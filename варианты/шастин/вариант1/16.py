import sys
sys.setrecursionlimit(5000)

def g(n):
    if n < 3:
        return n
    if n > 2:
        return n - 1 + g(n - 1)


print(g(4044))