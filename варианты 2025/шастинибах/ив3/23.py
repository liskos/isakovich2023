def f(a, b):
    if a == b:
        return 1
    if a < b:
        return 0
    return f(a - 2, b) + f(a - 20, b) + f(a // 3, b)

for i in range(10, 51):
    pass