def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b.replace('0', '1')
    else:
        b = b[b.find('1'):].replace('1', '00')
    return int(b, 2)
print(f(11))
for i in range(1, 1000):
    if f(i) <= 600:
        print(i)