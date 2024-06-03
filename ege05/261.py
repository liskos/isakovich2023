def f(n):
    b = bin(n)[2:]
    if b.rfind('0') != -1:
        i = b.rfind('0')
        b = b[:i] + b[0] + b[1] + b[i+1:]
    else:
        return 100000000
    b = b[::-1]
    return int(b, 2)

a = []
for i in range(2, 10000):
    if f(i) == 127:
        a.append(f(i))
print(len(a))