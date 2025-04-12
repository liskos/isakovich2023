def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    b = [x for x in a if x % 10 == 7 and x != n and x != 7]
    return b
k = 0
for i in range(1125000, 10**10):
    if len(f(i)) > 1:
        k += 1
        print(i, min(f(i)))
    if k == 5:
        break