def f(a, b):
    if a > b or a == 21:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 2, b) + f(a * 3, b)

def g(a, b):
    if a > b or a == 15:
        return 0
    if a == b:
        return 1
    return g(a + 1, b) + g(a + 2, b) + g(a * 3, b)


print(f(6, 15) * f(15,25) + g(6, 21) * g(21, 25))