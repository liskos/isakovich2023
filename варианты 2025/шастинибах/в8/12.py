def f(s):
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '522', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    return s


c = []
for i in range(3, 2000):
    if f('2' + i * '5').count('2') == 10:
        c.append(i)
print(min(c))