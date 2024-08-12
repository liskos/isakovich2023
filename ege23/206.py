def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if (a * 10 + 1) % 3 == 0:
        return f(a + 1, b) + f(a * 10 + 1, b) + f(a * 5, b)
    else:
        return f(a + 1, b) + f(a * 5, b)

print(f(1, 410))