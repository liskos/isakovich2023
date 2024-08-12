def f(a, b, c):
    if c > 7:
        return 0
    if a == b:
        return 1
    return f(a + 1, b, c + 1) + f(a * 2, b, c + 1) + f(a - 3, b, c + 1)

print(f(1, 10, 0))