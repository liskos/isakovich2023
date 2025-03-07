def f(n):
    a = []
    while n > 0:
        a.append(str(n % 7))
        n = n // 7
    return ''.join(a)[::-1]



a = []

for x in range(1, 2031):
    r = 7 ** 170 + 7 ** 100 - x
    if f(r).count('0') == 73:
        print(x)


