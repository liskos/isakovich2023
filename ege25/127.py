def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


for i in range(1523467, 4157813):
    if len(f(i)) == 3:
        print(i, max(f(i)))