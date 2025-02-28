def f(n):
    a = set()
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a

k = 0
for i in range(394480, 394540):
    z = f(i)
    if len(z) % 2 > 0:
        k += 1
        print(len(z), *sorted(z, reverse=True)[:2])

