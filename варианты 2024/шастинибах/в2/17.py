a = [int(x) for x in open('17.txt')]
c = []
d = [x for x in a if 100 > x > 9]
for i in range(len(a) - 1):
    if (a[i] % 10) + (a[i+1] % 10) == len(d):
        c.append(a[i] + a[i+1])
print(len(c), min(c))