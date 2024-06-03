def f(n):
    b = hex(n // 2)[2:]
    if n % 4 == 1:
        b = 'F' + b + 'A0'
    else:
        b = '15' + b + 'C'
    return int(b, 16)

a = []
for i in range(1, 10000):
    if f(i) < 65536:
        a.append(i)
print(max(a))