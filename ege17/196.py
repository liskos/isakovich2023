
a = [int(x) for x in open('17data/17-10.txt')]
c = []
for i in range(len(a) - 2):
    t = sorted(a[i:i+3])
    if t[0] ** 2 + t[1] ** 2 == t[2] ** 2:
        c.append(t[2])
print(len(c), sum(c))