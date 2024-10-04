def f(n):
    while ('90' in n) or ('300' in n) or ('000' in n):
        if '90' in n:
            n = n.replace('90', '0', 1)
        if '300' in n:
            n = n.replace('300', '09', 1)
        if '000' in n:
            n = n.replace('000', '3', 1)
    return n


a = []

for i in range(4, 10000):
    s = '9' + i * '0'
    if f(s).count('9') == 2:
        a.append(i)
print(len(a))

