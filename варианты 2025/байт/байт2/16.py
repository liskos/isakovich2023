import sys

sys.setrecursionlimit(5000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n + 1) * f(n - 1)
print((f(2025) // 2026 + f(2024)) // f(2023))