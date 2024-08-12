def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 2, b)

n1 = f(11, 17) * f(17, 29)
n2 = f(11, 23) * f(23, 29)
n3 = f(11, 17) * f(17, 23) * f(23, 29)
print(n1 + n2 - n3)