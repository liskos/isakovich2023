def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    b = [x for x in a if x % 1000 == 134 and x != 134]
    return b
k = 0
for i in range(30000000, 10**10):
    if len(f(i)) > 0:
        print(i, min(f(i)))
        k+=1
    if k == 5:
        break