def f(n):
    b = bin(n)[2:]
    while len(b) < 0:
        b = '0' + b
    s = b[::-1]
    return int(b, 2) - int(s, 2)

a = []
for i in range(1, 256):
    if f(i):
        a.append(f(i))
print(max(a))
