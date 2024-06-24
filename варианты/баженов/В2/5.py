def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '11' + b[2:] + '10'
    else:
        b = b + b[:3]
    if int(b, 2) % 2 == 0:
        b = b[:2] + b[3:]
    else:
        b = b[:4] + b[5:]
    return int(b, 2)

a = set()
for i in range(1, 10000):
    if 800 <= f(i) <= 1600:
        a.add(i)
print(len(a))
