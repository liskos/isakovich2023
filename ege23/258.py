def f(a, b):
    if a > b or a == 32:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a + 5, b) + f(a * 2, b)

def g(a, b):
    if a > b or a == 16:
        return 0
    if a == b:
        return 1
    return g(a + 3, b) + g(a + 5, b) + g(a * 2, b)


print(f(4, 16) * f(16,68) + g(4, 32) * g(32, 68))