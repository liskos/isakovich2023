def f(a, b, c):
    if a > b or c > 2:
        return 0
    if a == b:
        return 1
    if a % 2 == 0:
        return f(a + 2, b, c) + f(a * 2 + 1, b, c + 1)
    else:
        return f(a + 2, b, c) + f(a * 2, b, c)



print(f(2, 35, 0))