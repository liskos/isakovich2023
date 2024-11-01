import fnmatch
def f(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n//i)
    return a


for i in range(990000, 1000000):
    d = f(i)
    if any(fnmatch.fnmatch(str(x), '1??56*5') for x in d):
        print(i, min([x for x in d if fnmatch.fnmatch(str(x), '1??56*5')]))