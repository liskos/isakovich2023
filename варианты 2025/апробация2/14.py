def f(n):
    a = []
    while n > 0:
        a.append(str(n % 3))
        n = n // 3
    return ''.join(a)[::-1]


for x in range(1, 2031):
    r = 3 ** 100 - int(f(x))
    if str(f(r)).count('0') == 1:
        print(r, x)