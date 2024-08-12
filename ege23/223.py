def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return "BCA" in c
    return f(a + 1, b, c + "A") + f(a * 2, b,c + 'B') + f(a * 3, b, c + 'C')
print(f(2, 27,''))