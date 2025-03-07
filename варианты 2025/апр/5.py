def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    return int(b, 2)

a = []
for i in range(1, 10000):
    if i <= 12:
        a.append(f(i))
print(max(a))