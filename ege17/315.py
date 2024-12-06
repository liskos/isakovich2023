def f(a, b):
    return '101010' in bin(a * b)[2:]

a = [int(x) for x in open('17data/17-304.txt')]
sr = sum([x for x in a]) // len([x for x in a])
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) and a[i] + a[i+1] > sr:
        c.append(a[i] + a[i+1])
print(len(c), min(c))