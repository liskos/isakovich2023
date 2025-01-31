def a(n):
    c = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            c.add(i)
            c.add(n // i)
    c.add(1)
    return sum(c)//(len(c))

k = 0
for i in reversed(range(1, 770000)):
    if a(i) % 100 == 12:
        print(i, a(i))
        k += 1
        if k == 5:
            break
