def f(a, b, c):
    if a > b or c > 5:
        return 0
    if a == b:
        return 1
    return f(a + 1, b, c) + f(a * 3, b, c + 1) + f(a * 4, b, c + 1)

print(f(3, 300, 0))