def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a

for i in range(500000, 10**12):
    if sum(f(i)) % 10 == 9:
        print(i, sum(f(i)))