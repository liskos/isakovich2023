import fnmatch


def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    b = [x for x in a if x % 2 > 0]
    return b


for i in range(1, 10**7):
    if fnmatch.fnmatch(str(i), '14?4*') and i % 217 == 0:
        print(i, sum(f(i)))