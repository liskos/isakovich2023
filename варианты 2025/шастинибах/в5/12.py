def f(s):
    while '766' in s or '667' in s:
        if '766' in s:
            s = s.replace('766', '67', 1)
        if '667' in s:
            s = s.replace('667', '7', 1)
    return s

c = set()
for i in range(3, 3000):
    c.add(f('7' + i * '6'))
print(len(c))