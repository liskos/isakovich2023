def tr(a):
    s = []
    while a >0:
        s.append(str(a%3))
        a = a // 3
    return ''.join(s[::-1])



def f(n):
    b = tr(n)[2:]
    if n % 3 == 0:
        b = b + b[-2:]
    else:
        b = b + tr(b.count('1') + b.count('2') + b.count('2'))
    return int(b, 3)


c = []
for i in range(10, 1000, 2):
    if f(i) > 220:
        c.append(f(i))
print(min(c))
