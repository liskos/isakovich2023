import sys

sys.setrecursionlimit(5000)

def f(n):
    if n > 7000:
        return n + 4
    if n <= 7000:
        return 3 * n + 5 + f(n + 3)
print(f(707) - f(716))