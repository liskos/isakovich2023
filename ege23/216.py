def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return 1
    if a == 2:
        return f(a + 1, b, a) + f(a * 3, b, a)
    else:
        return f(a + 1, b, a) + f(a * 3, b, a) + f(a + c,b,a)

print(f(2, 27, 0))