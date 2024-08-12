def f(a, b, c):
    if a % 6 == 0:
        c += 1
    if a > b or c > 3:
        return 0
    if a == b:
        return 1
    return f(a + 2, b, c) + f(a * 2, b, c) + f(a * 3, b, c)

print(f(1, 300, -1))