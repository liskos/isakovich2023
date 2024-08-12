def f(a, b, c):
    if c > 8:
        return 0
    if a == b and c == 8:
        return 1
    return f(a + 3, b, c + 1) + f(a - 1, b, c + 1)

print(f(5, 5, 0))