def f(a, b, c):
    if a == b and c == 8:
        return 1
    if a > b or c > 8:
        return 0
    return f(a + 1, b, c + 1) + f(a * 2, b, c + 1) + f(a * 3, b, c + 1)


print(f(1, 34,0))