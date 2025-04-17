def ch(n):
    a = []
    while n > 0:
        a.append(str(n % 4))
        n = n // 4
    return ''.join(a)[::-1]


def f(n):
    b = ch(n)
    if sum([int(x) for x in b]) % 2 == 0:
        b = '13' + b[2:] + '0'
    else:
        b = '2' + b[:-2] + '13'
    return int(b, 4)
a = []
for i in range(1, 1000):
    if f(i) == 167:
        a.append(i)
print(min(a))