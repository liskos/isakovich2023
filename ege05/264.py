def f(n):
    if n % 2 == 0:
        n = n // 2
    else:
        n = n - 1
    if n % 5 == 0:
        n = n // 5
    else:
        n = n - 1
    if n % 7 == 0:
        n = n // 7
    else:
        n = n - 1
    return n

a = set()
for i in range(1, 10000):
    if f(i) == 6:
        a.add(i)
print(len(a))

