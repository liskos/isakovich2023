def f(a, b, c):
    if a > b or c > 2:
        return 0
    if a == b:
        return 1
    return f(a + 1, b, c) + f(a * 2, b, c + 1) + f(a * 3, b, c + 1)

print(f(1, 100, 0))