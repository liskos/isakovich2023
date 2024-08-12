def f(a, b, c, d, g):
    if a > b or c > 4 or g > 5:
        return 0
    if a == b:
        return d >= 2 and g == 5
    return f(a * 5, b, c + 1, d, g) + f(a * 3, b, c, d + 1, g) + f(a + 45, b, c, d, g + 1)


print(f(1, 2970, 0, 0, 0))