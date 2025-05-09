def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b.replace('0', '1')
    else:
        b = "1" + b[1:].replace('1', '00')
    return int(b, 2)
print(f(11)==32)
a = []
for i in range(1, 1000):
    if f(i) <= 600:
        a.append([i, f(i)])
a.sort(key=lambda x:(x[1],x[0]), reverse=True)
print(a)