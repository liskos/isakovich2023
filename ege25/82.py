def f(n):
    a = set()
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    a.add(1)
    return a
import itertools


for i in range(300, 351):
    a = f(i)
    for j in range(1, len(a) + 1):
        x = [sum(z) for z in itertools.combinations(a, r=j)]
        if i in x:
            print(i)
            break


