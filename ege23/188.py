def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a % 2 == 1:
        return f(a * 2, b)
    else:
        return f(a + 1, b) + f(a + 2, b)

print(f(2, 20) * f(20, 38) * f(38, 76))