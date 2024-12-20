import fnmatch
def f(n):
    a = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    b = [x for x in a if x % 2 == 0]
    return b


c = []
for x in range(65000,100000000, 2):
    a = f(x)
    if fnmatch.fnmatch(str(x), '6*97*5?') and len(a) >= 4:
        c.append(x)
        print(x, sum(a))
    if len(c) == 7:
        break
