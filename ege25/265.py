
def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a



for i in range(100000000, 1000000001, 2):
    if len(f(i)) == 39:
        print(i, max([x for x in f(i) if x % 2 > 0]))
