def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
            break
    return min(a) if a else 0

k = 0
for i in reversed(range(2022, 20222023)):
    if f(i) > 100:
        k += 1
        print(i, f(i))
    if k == 5:
        break