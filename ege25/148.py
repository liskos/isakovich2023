def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    b = [x for x in a if x % 2 == 0]
    return b
def g(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a


for i in range(113000000, 114000001):
    z = f(i)
    h = g(i)
    if len(z) == 3:
        d = [x for x in h if x < max(h)]
        print(i, max(d), h)