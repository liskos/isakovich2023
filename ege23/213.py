def f(a, b, c):
    if a % 2 == 1 and c % 2 == 1:
        return 0
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 2, b, a) + f(a * 3, b, a) + f(a * 4, b, a)

print(f(1, 600, 0))