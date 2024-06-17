def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b[:4].replace('1', '2').replace('0','1').replace('2','0') + b[4:]
    else:
        b = b[0] + b[1:4].replace('1','2').replace('0','1').replace('2','0') + b[-1]
    return int(b, 2)


a = []
for i in range(1, 10000):
    if f(i) > 63:
        a.append(i)
print(min(a))