def f(a, b, c):
    if a == 17 or a == 19 or a == 23 or a == 29 or a == 31:
        c += 1
    if a > b:
        return 0
    if a == b:
        return c == 3
    return f(a + 2, b, c) + f(a + 3, b, c)
print(f(15, 34, 0))