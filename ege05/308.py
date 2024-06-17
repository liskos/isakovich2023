def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b =b[:-4] + b[-4:].replace('1', '2').replace('0','1').replace('2','0')
    else:
        b = b[:-5] + b[-5:-1].replace('1','2').replace('0','1').replace('2','0') + b[-1]
    return int(b, 2)

print(f(36))
print(f(37))
a = []
for i in range(1, 10000):
    if f(i) == 64:
        a.append(i)
        print(i)
