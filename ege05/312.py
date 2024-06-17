def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '1' + b + '00'
    else:
        b = b + bin(b.count('1'))[2:]
    return int(b, 2)

a = []
for i in range(9, 10000):
    if f(i) > 88:
        a.append(i)
print(min(a))