def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a * 2, b)
print(f(3, 20) * f(20, 43) + f(3, 20) * f(20, 47) + f(7, 20) * f(20, 43) + f(7, 20) * f(20, 47))