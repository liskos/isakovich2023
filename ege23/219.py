def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return 1
    if c == 30:
        return f(a * 2, b, c) + f(a * 3, b, c)
    return f(a + 1, b, c + 1) + f(a * 2, b, c) + f(a * 3, b, c)
print(f(1, 9217, 0))