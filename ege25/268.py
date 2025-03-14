
def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a



for i in range(35000000, 100000000):
    if len(f(i)) == 3:
        print(i, max(f(i)))
