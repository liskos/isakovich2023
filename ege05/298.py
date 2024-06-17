def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b[1:]
    else:
        b = '1' * b.count('1') + '1'
    if b.count('1') % 2 == 0:
        b = b[1:]
    else:
        b = '1' * b.count('1') + '1'
    return int(b, 2)
print(f(5))
a = []
for i in range(2, 1000):
    if f(i) == 7:
        a.append(i)
print(len(a))