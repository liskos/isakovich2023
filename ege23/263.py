def f(a, b):
    if b > 4:
        return 0
    if b == 4:
        c.add(a)
    return f(a + 2, b + 1) + f(a * 3, b + 1)

c = set()
f(1, 0)
print(len(c))