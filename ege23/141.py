def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    if a % 3 == 0:
        return f(a - 2, b)
    else:
        return f(a - 2, b) + f(a - a % 3, b)


print(f(23, 3))