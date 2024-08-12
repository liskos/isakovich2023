def f(a, b):
    if b == 17:
        c.add(a)
    else:
        if a > 0 and a ** 0.5 == int(a ** 0.5):
            f(int(a) ** 0.5, b + 1)
        f(a - 1, b + 1)
        f(a - 2, b + 1)
c = set()
f(113, 0)
print(len(c))