def f(a, b, c):
    if a > b or c <= 0:
        return 0
    if a == b:
        return 1
    return f(a + 3, b, c - a) + f(a * 4, b, c - a) + f(a * 5, b, c - a)

print(f(1, 2000, 500))