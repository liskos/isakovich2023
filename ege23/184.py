def f(a, b):
    if b == 9:
        if a > 0:
            c.add(a)
    else:
        f(a - 3, b + 1)
        f(a * (-3), b + 1)
c = set()
f(133, 0)
print(len(c))