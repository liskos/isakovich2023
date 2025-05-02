def f(n):
    b = bin(n)[2:]
    b = b + bin(b.count('1') % 2)[2:]
    b = b + bin(b.count('1') % 2)[2:]
    return int(b, 2)

print(f(12), f(7))

for i in range(1, 1000):
    if f(i) > 253:
        print(i)
        break