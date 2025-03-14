import fnmatch



def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a



for i in range(1, 10**10):
    if fnmatch.fnmatch(str(i), '4*1?009') and i ** 2 <= 10 ** 10:
        print(i, i ** 2)