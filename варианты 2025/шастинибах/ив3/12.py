def f(s):
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '522', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    return s

a = []
for i in range(4, 1000):
    r = f('2' + i * '5')
    if r.count('2') == 10:
        a.append(sum(map(int, r)))
print(max(a))