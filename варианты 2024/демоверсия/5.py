def f(n):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        s = s + bin(n % 3 * 3)[2:]
    return int(s, 2)

a = []
print(f(12), f(4))
for i in range(1, 10000):
    if f(i) > 151:
        a.append(f(i))
print(min(a))