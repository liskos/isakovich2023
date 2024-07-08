c = set()


def f(a, b):
    if b == 6:
        if 34 <= a <= 59:
            c.add(a)
    else:
        f(a + 1, b + 1)
        f(a + 2, b + 1)
        f(a * 2, b + 1)

f(1, 0)
print(len(c))