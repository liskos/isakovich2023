import fnmatch


def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a


for i in range(10000, 10**7):
    if fnmatch.fnmatch(str(i), '?6*6*?6') and i % 6 == 0 and i % 7 == 0 and i % 8 == 0:
        print(i, sum(f(i)))