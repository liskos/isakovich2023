def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(int('1' + bin(a)[2:], 2), b)


print(f(4, 49))