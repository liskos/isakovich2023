def f(a, b, c, d, g):
    if a > b:
        return 0
    if a == b:
        return c > 0 and d > 0 and g > 0
    return f(a + 1, b, c + 1, d, g) + f(a + 2, b,c, d + 1, g) + f(a * 2, b, c, d, g + 1)
print(f(3, 25,0,0,0))