def f(a, b):
    if a == b:
        return 1
    if a > b or a == 22:
        return 0
    return f(a + 1, b) + f(a * 2, b)


print(f(5, 8) * f(8, 60))