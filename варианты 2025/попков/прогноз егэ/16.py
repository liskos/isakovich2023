import sys
sys.setrecursionlimit(50000)


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (4 * n - 3) * f(n-1)

print((f(5168)//11 + f(5166))//(f(5165)))