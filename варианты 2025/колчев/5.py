def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = '1' + b[:-2] + '11'
    else:
        b = '10' + b + '0'
    return int(b, 2)
print(f(4) == 40, f(6) == 15)
a = []
for i in range(2, 1000, 2):
    if f(i) > 999:
        a.append(f(i))
print(min(a))