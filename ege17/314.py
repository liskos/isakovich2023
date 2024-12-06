def f(a, b):
    return 'aa' in hex(a)[2:] and 'aa' in hex(b)[2:]

a = [int(x) for x in open('17data/17-304.txt')]
sr = max([x for x in a if x % 246 == 0])
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) and a[i] + a[i+1] > sr:
        c.append(a[i] + a[i+1])
print(len(c), max(c))