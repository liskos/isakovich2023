def f(s):
    n = []
    while s > 0:
        n.append(str(s % 7))
        s = s // 7
    return ''.join(n)

a = [int(x) for x in open('17data/17-243.txt')]
ma = max([x for x in a if x % 107 == 0])
c = []
for i in range(len(a) - 1):
    if ('36' in f(a[i]) or '36' in f(a[i+1])) and (a[i] > ma or a[i+1] > ma):
        c.append(a[i] + a[i+1])
print(len(c), min(c))