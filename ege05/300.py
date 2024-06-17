def f(n):
    b = bin(n)[2:]
    b = b[b.find('1'):] + b[:b.find('1') + 1]
    if b.count('1') % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '0'
    return int(b, 2)

a = []
for i in range(2, 1000):
    if f(i) < 450:
        a.append(i)
print(max(a))