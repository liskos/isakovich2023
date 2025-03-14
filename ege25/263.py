import fnmatch



def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a



for i in range(1, 10**9):
    if fnmatch.fnmatch(str(i), '15*3*09') and len(f(i)) == 7:
        print(i, max(f(i)))