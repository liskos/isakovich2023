
def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    b = [x for x in a if x % 2 > 0]
    return b



for i in range(35000000, 100000000):
    if len(f(i)) == 5:
        print(i, max(f(i)))
