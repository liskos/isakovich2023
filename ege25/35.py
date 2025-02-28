def f(n):
    a = set()
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


m = set()
for i in range(394480, 394540):
    z = f(i)
    m.add(len(z))
    if len(z) == 48:
        print(len(z), *sorted(z, reverse=True)[:2])
print(max(m))
