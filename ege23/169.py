def f(a, b, c):
    if c > 9:
        return 0
    if a == b and 1 <= c <= 9:
        return 1
    return f(a + 3, b, c + 1) + f(a - 1, b, c + 1)

print(f(5, 5, 0))