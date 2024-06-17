def f(n, m):
    s1 = bin(n)[2:].count('1') ** 2
    s2 = bin(m)[2:].count('1') ** 2
    return s1 - s2


for i in range(1, 10000):
    if f(i, p) == 33:
        print(i)
        break
