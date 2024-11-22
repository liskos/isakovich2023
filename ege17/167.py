

a = [int(x) for x in open('17data/17-3.txt')]
c = []
for i in range(len(a) - 3):
    if a[i] % 2 != a[i+1] % 2 != a[i+2] % 2 != a[i+3] % 2:
        c.append(a[i] + a[i+1] + a[i+2] + a[i+3])
print(len(c), max(c))