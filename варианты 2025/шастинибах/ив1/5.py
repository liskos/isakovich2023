def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '11' + b[2:] + '1'
    elif b.count('1') % 2 > 0:
        if b.count('1') > b.count('0'):
            b = b + '0'
        else:
            b = b + '1'
    return int(b, 2)

print(f(6))
print(f(4))
a = []

for i in range(1, 1000):
    if f(i) > 271:
        a.append(i)
print(min(a))