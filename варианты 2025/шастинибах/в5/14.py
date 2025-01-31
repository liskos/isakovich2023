def f(a):
    c = []
    while a > 0:
        c.append(a%7)
        a = a // 7
    return ''.join(str(c[::-1]))
d = []
for x in range(1, 100):
    if f(7 ** 666 + 7 ** 333 + 49 ** x - 343).count('6') == 49:
        d.append(x)
print(min(d))
