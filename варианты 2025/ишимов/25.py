def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    if len(a) > 0:
        return max(a) - min(a)
    else:
        return 0
k = 0

for i in reversed(range(1, 1533879)):
    if f(i) > 5000 and f(i) % 1235 == 0:
        k += 1
        print(i, f(i))
        if k == 5:
            break
