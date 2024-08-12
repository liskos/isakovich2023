def f(a, b, c):
    if a % 2 == 0:
        c += 1
    if a > b or c > 2:
        return 0
    if a == b:
        return 1
    return f(a + 2, b, c) + f(a * 2, b, c) + f(a * 3, b, c)

print(f(1, 402, -1))