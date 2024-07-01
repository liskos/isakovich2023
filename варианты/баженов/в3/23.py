def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 4, b) + f(a + 7, b)

print(f(2, 15) + f(2, 12) + f(2, 9))