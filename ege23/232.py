def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a * 4, b) + f(a * 5, b)

def h(a, b, c):
    if a > b:
        return 0
    if a == b:
        return c <= 4
    else:
        return h(a + 3, b, c + 1) + h(a * 4, b, c) + h(a * 5, b, c)

print(f(1, 16) * h(16, 140, 0) * f(140, 725))