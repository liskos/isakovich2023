
a = [int(x) for x in open('17data/17-354.txt')]
m = min([x for x in a if x % 10 == 3])
s = max([x for x in a if x % 100 == 52])
c = []
for i in range(len(a) - 1):
    if a[i] % 10 == 3 and not(a[i+1] % 10 == 3) and a[i] ** 2 + a[i+1] ** 2 < m ** 2:
        c.append(a[i] ** 2 + a[i+1] ** 2)
print(len(c), max(c))