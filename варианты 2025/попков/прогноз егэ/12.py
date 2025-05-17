def f(s):
    while '40' in s or '800' in s or '000' in s:
        if '40' in s:
            s = s.replace('40', '0', 1)
        if '800' in s:
            s = s.replace('800', '04', 1)
        if '000' in s:
            s = s.replace('000', '8', 1)
    return s


for n in range(3, 10000):
    r = f('4' + n * '0')
    if sum(map(int, r)) == 36:
        print(n)