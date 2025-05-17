def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '10' + b + '0'
    else:
        b = '1' + b + '11'
    return int(b, 2)
print(f(4), f(5))
a = []
for i in range(1, 1000):
    if f(i) < 410:
        a.append(f(i))
print(max(a))