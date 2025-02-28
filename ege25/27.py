def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a

for i in range(125873, 136762 + 1):
    z = f(i)
    if len(z) == 5:
        print(i, *sorted(z))