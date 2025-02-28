def f(n):
    a = 0
    d = 1
    c = [a, d]
    while n > 0:
        a += n % 10
        d *= n % 10
        n = n // 10
    return c



for i in range(87921, 88188):
    if f(i)[0] % 14 == 0 and f(i)[1] % 18 == 0 and f(i)[1] != 0:
        print(*sorted(f(i), reverse=True))


