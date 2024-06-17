def f(n, m):
    s1 = bin(n)[2:].count('1') ** 2
    s2 = bin(m)[2:].count('1') ** 2
    return s1 - s2

a = []
for i in range(1, 1000):
    for m in range(1, 1000):
        if f(i, m) == 33:
            a.append(i + m)
print(min(a))
