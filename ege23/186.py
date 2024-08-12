def f(a, b):
    if b == 7:
        if a >= 0:
            c.add(a)
    else:
        f(a - 5, b + 1)
        f(a * (-2), b + 1)
c = set()
f(216, 0)
print(len(c))