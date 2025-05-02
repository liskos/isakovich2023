def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sum(a)
k = 0
for i in range(500001, 10**10):
    if f(i) % 10 == 6:
        print(i, f(i))
        k += 1
    if k == 5:
        break

