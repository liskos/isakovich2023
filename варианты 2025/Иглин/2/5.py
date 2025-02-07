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
        b = b + sh(sum(int(i) for i in b))
    return int(b, 6)

print(f(11), f(12))
c = []
for i in range(25, 1000):
    if f(i) % 2 == 0:
        c.append(f(i))
print(min(c))