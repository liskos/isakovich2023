def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a == 6:
        return f(a + 1, b) + f(a + 3, b) + f(8, b)
    if a == 7:
        return f(a + 1, b) + f(a + 3, b) + f(13, b)
    if a == 8:
        return f(a + 1, b) + f(a + 3, b) + f(21, b)
    else:
        return f(a + 1, b) + f(a + 3, b)


print(f(6, 21))