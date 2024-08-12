def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a - 3, b) + f(a // 7, b)
print(f(50, 1))