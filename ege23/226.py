def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return "BBA" not in c
    return f(a * 2, b, c + "A") + f(a + 2, b,c + 'B')
print(f(4, 42,''))