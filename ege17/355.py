
a = [int(x) for x in open('17data/17-354.txt')]
m = min([x for x in a if x % 10 == 3])
s = max([x for x in a if x % 10 == 5])
c = []
for i in range(len(a) - 1):
    if a[i] % 10 == 8 and not(a[i+1] % 10 == 8) and a[i] ** 2 + a[i+1] ** 2 > s ** 2:
        c.append(a[i] ** 2 + a[i+1] ** 2)
print(len(c), min(c))