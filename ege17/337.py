
a = [int(x) for x in open('17data/17-336.txt')]
sr = max([x for x in a if x % 37 == 0])
c = []
for i in range(len(a) - 1):
    if (a[i] % sr == 0 or a[i] % sr == 0) and (a[i] + a[i+1]) % sr > 30:
        c.append(a[i] + a[i+1])
print(len(c), min(c))