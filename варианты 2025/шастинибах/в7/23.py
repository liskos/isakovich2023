def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    k = f(a - 1, b)
    if a % 2 == 0:
        k += f(a // 2, b)
    if a % 3 == 0:
        k += f(a // 3, b)
    return k

print(f(122, 57) * f(57, 11))