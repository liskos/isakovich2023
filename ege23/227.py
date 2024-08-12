def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return "BACA" not in c
    return f(a + 2, b, c + "A") + f(a * 2, b,c + 'B') + f(a * 4, b, c + 'C')
print(f(1, 24,''))