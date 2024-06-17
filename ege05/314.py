def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '101' + b[3:] + '0'
    else:
        b = '10' + b[2:] + '11'
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) > 68:
        a.append(i)
print(min(a))