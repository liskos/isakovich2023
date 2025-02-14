def f(s):
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>')
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    return s

c = []
a = 11111111111111111112222222222222222222222222222222
for i in range(6, 101):
    c.append(f('>' + 19 * '0' + i * '1' + 19 * '2'))
d = 0
while a > 0:

    d += a % 10
    a = a // 10
print(d)