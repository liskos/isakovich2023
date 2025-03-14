
def p(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n , i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b
def e(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    b = [x for x in a if x % 2 == 0]
    return b

for i in range(100000000, 10**10):
    if len(p(i)) == len(e(i)):
        print(i, abs(sum(p(i)) - sum(e(i))))