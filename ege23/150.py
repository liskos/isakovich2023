def f(a):
    if a < 100:
        if a % 2 == 0:
            b.add(a)
        f(a + 3)
        f(a * 3)
b = set()
f(3)
print(len(b))