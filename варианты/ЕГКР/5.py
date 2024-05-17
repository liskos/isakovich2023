def f(n):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = s + s[-2] + s [-1]
    if n % 2 == 1:
        s = '1' + s + '0'
    return int(s, 2)

print(f(11),f(10))
a = []
for i in range(1, 100000):
    if f(i) < 100:
        a.append(i)

print(max(a))