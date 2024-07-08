c = set()


def f(a, b):
    if b == 4:
        c.add(a)
    else:
        f(a + 1, b + 1)
        f(a + 5, b + 1)
        f(a * 3, b + 1)

f(1, 0)
print(len(c))