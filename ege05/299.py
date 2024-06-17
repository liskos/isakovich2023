def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b[1:]
        while b[0] == '0':
            b = b[1:]
    else:
        b = '1' + b + '00'
    if b.count('1') % 2 == 0:
        b = b[1:]
        while b[0] == '0':
            b = b[1:]
    else:
        b = '1' + b + '00'
    return int(b, 2)

a = []
for i in range(2, 1000):
    if f(i) > 100:
        a.append(i)
print(min(a))