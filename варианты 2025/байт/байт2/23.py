def f(a, b):
    if a == b:
        return 1
    if a < b or a == 15:
        return 0
    return f(a - 2, b) + f(a - 5, b) + f(a // 3, b)

print(f(50, 35) * f(35, 20) * f(20, 8))