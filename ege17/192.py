def f(n):
    s = 0
    if 100 > n > 9:
        s += n % 10 + n // 10
    if n >= 100:
        s += n % 10 + n // 10 + n // 10 % 10
    if n < 10:
        s += n
    return s

a = [int(x) for x in open('17data/17-7.txt')]
c = []
for i in range(len(a)):
    if f(a[i]) % 3 == 0:
        c.append(a[i])
print(len(c), max(c))