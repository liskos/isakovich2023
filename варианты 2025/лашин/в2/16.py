import sys

sys.setrecursionlimit(50000)

def f(n):
    if n < 5:
        return n + 5
    if n > 4:
        return f(n - 2) * 2 * n

print((f(12025) + f(12023)) // f(12021))