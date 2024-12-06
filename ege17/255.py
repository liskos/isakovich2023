def f(s):
    n = []
    while s > 0:
        n.append(str(s % 3))
        s = s // 3
    return ''.join(n)

a = [int(x) for x in open('17data/17-243.txt')]
ma = max([x for x in a if x % 173 == 0])
c = []
for i in range(len(a) - 1):
    if ('22' in f(a[i]) or '22' in f(a[i+1])) and (a[i] > ma or a[i+1] > ma):
        c.append(a[i] + a[i+1])
print(len(c), min(c))