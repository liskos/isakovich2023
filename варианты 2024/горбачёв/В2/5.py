def de(a):
    b = []
    while a > 0:
        b.append(str(a % 9))
        a = a // 9
    return ''.join(b)


def f(n):
    b = de(n)
    if b.count('1') % 2 == 0:
        b = b + '52'
    else:
        b = '73' + b[2:] + '44'
    return int(b, 9)


c = []
for i in range(1, 1000):
    if f(i) > 13950:
        c.append(i)
print(min(c))