def f(a,c):
    if c == 13:
        b.add(a)
    else:
        f(a + 3, c + 1)
        f(a * 2 + 1, c + 1)
b = set()
f(2, 0)
print(len(b))