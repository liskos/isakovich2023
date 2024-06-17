def f(n):
    b = bin(n)[2:]
    if b.count('1') % 4 == 0:
        b = '10' + b
    else:
        b = '11' + b
    if b[-1] == '1':
        b = b + '0'
    else:
        b = b + '1'
    return int(b,2)


a = []
for i in range(1, 10000):
    if f(i) <= 250:
        a.append(i)
print(max(a))