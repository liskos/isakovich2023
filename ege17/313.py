def f(a, b):
    return len(hex(a)[2:]) % 2 > 0 and len(hex(b)[2:]) % 2 > 0

a = [int(x) for x in open('17data/17-304.txt')]
sr = min([x for x in a if x % 321 == 0])
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) and a[i] + a[i+1] > sr:
        c.append(a[i] + a[i+1])
print(len(c), min(c))