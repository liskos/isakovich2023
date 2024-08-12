def f(a, b, c):
    if a > b or c > 3:
        return 0
    if a == b:
        return 1
    return f(a + 2, b, c) + f(a * 3, b, c + 1) + f(a * 5, b, c + 1)

print(f(2, 200, 0))