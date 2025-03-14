import fnmatch


def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a


for i in range(9005507, 10**7):
    if fnmatch.fnmatch(str(i), '9?*55*7'):
        print(i, sum(f(i)) % 21)