def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a

for i in range(258274, 258297 + 1):
    z = f(i)
    if len(z) == 4:
        print(i, *sorted(z))