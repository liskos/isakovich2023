def f(a, b):
    if a == b:
        return 1
    if a > b or a == 18 or a == 11:
        return 0
    return f(a + 1, b) + f(a + 2, b) + f(a * 3, b)


print(f(4, 8) * f(8, 23))