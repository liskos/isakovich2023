def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return "ABA" in c
    return f(a * 2, b, c + "A") + f(a + 3, b,c + 'B')
print(f(2, 38,''))