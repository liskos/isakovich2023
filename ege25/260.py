import fnmatch



def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a



for i in range(1, 10**7):
    if fnmatch.fnmatch(str(i), '3*52?') and len(f(i)) % 2 > 0:
        print(i, max(f(i)))