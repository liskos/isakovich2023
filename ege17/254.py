def f(a, b):
    return '3' in hex(a)[2:] or '3' in hex(b)[2:]


a = [int(x) for x in open('17data/17-243.txt')]
ma = max([x for x in a if x % 151 == 0])
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) and (a[i] > ma or a[i+1] > ma):
        c.append(a[i] + a[i+1])
print(len(c), min(c))