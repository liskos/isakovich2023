def f(n):
    b = bin(n)[2:]
    if b[-1] == '1' and b.count('1') % 2 == 1:
        b = '1' + b
    else:
        b = b + str(b.count('1') % 2)
    if b[-1] == '1' and b.count('1') % 2 == 1:
        b = '1' + b
    else:
        b = b + str(b.count('1') % 2)
    return int(b, 2)


a = []
for i in range(1, 10000):
    if f(i) < 100:
        a.append(i)
print(max(a))