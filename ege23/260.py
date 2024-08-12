def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a % 21 == 0:
        return f(a + 1, b)
    if a % 3 == 0:
        return f(a + 1, b) + f(a + 7, b)
    if a % 7 == 0:
        return f(a + 1, b) + f(a + 3, b)
    return f(a + 1, b) + f(a + 3, b) + f(a + 7, b)
print(f(13, 31))

