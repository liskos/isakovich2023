
def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    b = [x for x in a if x % 2022 == 0]
    return b



for i in range(100000000, 200000000):
    if len(f(i)) == 7:
        print(i, max(f(i)))
