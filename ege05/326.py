def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 1:
        x = '1'
    else:
        x = '0'
    if n % 2 == 0:
        b = '1' + b + x
    else:
        b = b + '0' + x
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) > 100:
        a.append(i)
print(min(a))