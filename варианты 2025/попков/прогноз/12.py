def f(s):
    while '444' in s or '777' in s:
        if '777' in s:
            s = s.replace('777', '4', 1)
        else:
            s = s.replace('444', '7', 1)
    return s

a = []
for n in range(3, 1001):
    r = f('4' + '7' * n)
    a.append(sum([int(x) for x in r]))
print(max(a))
