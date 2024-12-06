
a = [int(x) for x in open('17data/17-341.txt')]
sr = sum([x for x in a]) // len([x for x in a])
c = []
d = []
for i in range(len(a) - 3):
    if a[i] * a[i+1] > a[i+3] * a[i-1]:
        c.append(a[i] + a[i+1])
        if a[i] > sr or a[i+1] > sr:
            d.append(a[i])
print(max(c), len(d))