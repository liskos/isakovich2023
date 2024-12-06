

a = [int(x) for x in open('17data/17-243.txt')]
ma = sum([x for x in a if x % 49 == 0])
c = []
for i in range(len(a) - 1):
    if a[i] < ma and not(a[i+1] < ma):
        c.append(a[i] + a[i+1])
print(len(c), max(c))