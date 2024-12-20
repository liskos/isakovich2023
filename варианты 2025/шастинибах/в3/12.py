def f(s):
    while '411' in s or '1111' in s:
        if '411' in s:
            s = s.replace('411', '14', 1)
        if '1111' in s:
            s = s.replace('1111', '1', 1)
    return s


c = []
for i in range(1, 10000):
    c.append(sum(map(int, f('4' + '1' * i))))
print(max(c))