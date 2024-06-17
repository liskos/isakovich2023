def f(n):
    b = bin(n)[3:]
    if b.count('1') % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '0'
    return int(b, 2)


print(f(6))
a = []
for i in range(2, 10000):
    if f(i) < 450:
        a.append(f(i))
print(max(a))