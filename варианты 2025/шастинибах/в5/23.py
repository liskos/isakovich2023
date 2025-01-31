def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a + max(a % 10, a // 10), b)

print(f(10, 24)*f(24, 41))