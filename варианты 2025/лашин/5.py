def f(n):
    b = bin(n)[2:]
    if b.count('1') % 3 == 0:
        b = b + bin(b.count('1') % 5)[2:]
    else:
        b = '1' + b + '10'
    return int(b, 2)

c = []
for i in range(1, 10000):
    if f(i) > 89:
        c.append(f(i))
print(min(c))