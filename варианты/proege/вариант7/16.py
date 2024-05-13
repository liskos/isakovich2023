import sys

sys.setrecursionlimit(5000)


def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n - 2 + f(n - 1)


print(f(2024) - f(2022))