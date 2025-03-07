def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    b = [x for x in a if x % 2 > 0]
    return b


for i in range(63000000,  75000001):
    z = f(i)
    if len(z) == 5:
        print(i, max(z))