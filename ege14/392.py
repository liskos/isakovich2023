def f(n):
    a = []
    while n > 0:
        a.append(n % 6)
        n = n // 6
    return a

for x in range(17):
    r = int('3b801', 17) + (x * 17 ** 1) + int('20903', 17) + (x * 17 ** 1) + (x * 17 ** 3)
    if f(r).count(5) == 3:
        print(r, x)
