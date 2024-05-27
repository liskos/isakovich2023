def f(n):
    s = str(n) + str(n % 10)
    b = bin(int(s))[2:]
    if b.count('1') % 2 == 1:
        b = b + '1'
    else:
        b = b + '0'
    return int(b, 2)

print(f(13))
for i in range(1, 10000):
    if f(i) > 413:
        print(i)
        break