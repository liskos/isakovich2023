def f(a,b,c):
    if a == b or c == 15:
        return 1
    if a > b:
        return 0
    return f(a + 5, b, c + 1) + f(a * 2, b, c + 1)

print(f(0, 155, 0))