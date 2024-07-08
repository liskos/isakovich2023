def f(a, b, c):
    if a == b and c == i:
        return 1
    if a > b or c > i:
        return 0
    return f(a + 1, b, c + 1) + f(a + 5, b, c + 1) + f(a * 3, b, c + 1)

for i in range(1, 100):
    if (f(1, 227,0)) > 0:
        print(i)
        break