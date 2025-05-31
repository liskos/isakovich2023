def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '101' + b[3:] + '00'
    else:
        b = '110' + b[3:] + '10'
    return int(b, 2)

print(f(6))
print(f(4))
a = []
for i in range(1, 1000):
    if f(i) > 546:
        a.append(i)
print(min(a))