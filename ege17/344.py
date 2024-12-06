
a = [int(x) for x in open('17data/17-344.txt')]
m = min([x for x in a if x % 103 == 0])
s = max([x for x in a if x % 73 == 0])
c = []
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) % 2 == 0 and (a[i] - a[i+1]) % m:
        c.append(a[i] + a[i+1])
print(len(c), max(c))