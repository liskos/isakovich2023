
a = [int(x) for x in open('17data/17-1.txt')]
c = []
d = []
ma = max(a)
for i in range(len(a)):
    if a[i] == ma:
        c.append(a[i])
        d.append(i)
print(len(c), min(d))