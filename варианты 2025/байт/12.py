def f(s):
    while '211' in s or '1111' in s or '411' in s:
        if '211' in s:
            s = s.replace('211', '14', 1)
        if '1111' in s:
            s = s.replace('1111', '11', 1)
        if '411' in s:
            s = s.replace('411', '12', 1)
        return s

a = []
for i in range(3, 1000):
    if int(f('2' + '1' * i)) % 2 == 0:
        a.append(i)
print(max(a))