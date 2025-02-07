def sh(a):
    c = []
    while a > 0:
        c.append(str(a%6))
        a = a // 6
    return ''.join(c)[::-1]

def f(n):
    b = sh(n)
    if n % 3 == 0:
        b = b + b[::-1]
    else:
        b = b + str(sum(b))
    return int(b, 6)
c = []
for i in range(25, 1000, 2):
    c.append(f(i))
print(min(c))