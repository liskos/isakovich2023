
a = [int(x) for x in open('17data/17-352.txt')]
m = [x for x in a if x % 73 == 0]
s = max([x for x in a if x % 100 == 52])
c = []
for i in range(len(a) - 1):
    if a[i] >= any(m) and a[i+1] >= any(m):
        c.append(a[i] + a[i+1])
print(len(c), max(c))