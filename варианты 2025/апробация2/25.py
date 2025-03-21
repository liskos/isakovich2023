def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    if len(a) == 0:
        return 0
    else:
        return min(a) + max(a)

k = 0
for i in range(700000, 10**10):
    if f(i) % 10 == 4:
        k += 1
        print(i, f(i))
    if k == 5:
        break