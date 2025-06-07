def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    b = [x for x in a if x % 2 > 0]
    return sum(b) // len(b)
k = 0
for i in range(345678, 10**10):
    z = f(i)
    if z % 34 == 0 and z != 0:
        print(i, z)
        k += 1
        if k == 5:
            break