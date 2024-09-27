def f(a, b):
    if a > b or a == 22:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a + 4, b)

print(f(16, 38))