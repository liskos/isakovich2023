def f(n):
    b = bin(n)[2:]
    if b.count('0') % 2 == 0:
        b = '1' + b + '1'
    else:
        b = '10' + b
    return int(b, 2)

c = []
for i in range(1, 1000):
    if f(i) < 100:
        c.append(f(i))
print(max(c))