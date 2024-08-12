def f(a,c):
    if c == 11:
        b.add(a)
    else:
        f(a + 1, c + 1)
        f(a * 2 + 1, c + 1)
b = set()
f(3, 0)
print(len(b))