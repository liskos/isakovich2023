def f(a, b, c):
    if a == b and c == i:
        return 1
    if a > b or c > i:
        return 0
    return f(a + 1, b, c + 1) + f(a + 2, b, c + 1) + f(a * 2, b, c + 1)




for i in range(1, 100):
     h = (f(1, 28,0))
     if h > 0:
        print(h)
        break
