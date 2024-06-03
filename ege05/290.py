def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '1' + b + '00'
    else:
        b = '10' + b + '1'
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) == 21:
        a.append(i)
print(len(a))