def p(a):
    a += 1
    for i in range(2, a):
        if a % i == 0:
            return p(a)
    return a



def f(a, b):
    if a == b:
        return 1
    if a > b or a == 33:
        return 0
    return f(a + 2, b) + f(p(a), b)


print(f(2, 14) * f(14, 45))