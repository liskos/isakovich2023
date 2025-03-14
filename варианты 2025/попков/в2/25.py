def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


for i in range(178965, 178983):
    if len(f(i)) == 4:
        print(*sorted(f(i), reverse=True))