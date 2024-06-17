def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '11' + b[2:] + '00'
    else:
        b = '10' + b[2:] + '11'
    if b.count('1') % 2 == 0:
        b = '11' + b[2:] + '00'
    else:
        b = '10' + b[2:] + '11'
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) > 1500:
        a.append(f(i))
print(min(a))