def f(s):
    while '=3' in s or '=4' in s or '=5' in s:
        if '=3' in s:
            s = s.replace('=3', '55=', 1)
        if '=4' in s:
            s = s.replace('=4', '4=', 1)
        if '=5' in s:
            s = s.replace('=5', '3=', 1)
    return s.count('4') * 4 + s.count('5') * 5 + s.count('3') * 3


d = []
for i in range(1, 5000):
    if 9999 >= f('=' + 51 * '3' + i * '4' + 53 * '5') >= 1000:
        print(i)