def ch(a):
    c = []
    while a > 0:
        c.append(str(a % 4))
        a = a // 4
    return ''.join(c[::-1])



def f(n):
    b = ch(n)
    if n % 4 == 0:
        b = '2' + b + '03'
    else:
        b = b + ch(n % 4 * 5)
    return int(b, 4)

d = []
for i in range(1, 1000):
    if f(i) <= 567:
        d.append(i)
print(max(d))