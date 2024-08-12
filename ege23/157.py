def fac(a):
    c = 1
    for i in range(2, a + 1):
        c *= i
    return c
def f(a, b):
    if a > b or a == 12:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 4, b) + f(fac(a + 1), b)


print(f(2, 24))
