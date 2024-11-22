
a = [int(x) for x in open('17data/17-2.txt')]
c = []
d = []
mi = min(a)
for i in range(len(a)):
    if a[i] == mi:
        c.append(a[i])
        d.append(i)
print(len(c), max(d))