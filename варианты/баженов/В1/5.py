def f(n):
    s = bin(n)[2:]
    b = s.replace('0', '2').replace('1','0').replace('2','1')
    if n % 2 == 0:
        b = b + '10'
    else:
        b = b + '11'
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) > 125:
        a.append(f(i))
print(min(a))