import math

def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a


for i in range(1000000, 10**10):
    if sum(f(i)) % 2 > 0 and math.prod(f(i)) % 2 > 0 and len(f(i)) > 40:
        print(i, len(f(i)))