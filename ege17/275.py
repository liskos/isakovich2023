

a = [int(x) for x in open('17data/17-275.txt')]
ma = max([x for x in a])

c = []
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) % 11 == 0:
        c.append(a[i] + a[i+1])
print(len(c), max(c))