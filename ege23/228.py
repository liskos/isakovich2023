def f(a, b, c):
    if a < b:
        return 0
    if a == b:
        return "?B*C??" in c
    return f(a - 2, b, c + "A") + f(a - 3, b,c + 'B') + f(a // 2, b, c + 'C')
print(f(29, 2,''))