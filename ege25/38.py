def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a
m = set()
for i in range(248015, 251575):
    m.add(sum(f(i)))
    z = f(i)
    if len(z) == 4 and sum(f(i)) == 1045440:
        print(len(z), *sorted(z, reverse=True)[:2], max(m))