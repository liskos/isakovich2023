def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    b = [x for x in a if x % 2 > 0]
    return b

for i in range(190061, 190080 + 1):
    z = f(i)
    if len(z) == 4:
        print(i, *sorted(z, reverse=True))