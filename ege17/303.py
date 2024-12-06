

a = [int(x) for x in open('17data/17-303.txt')]
m = max([x for x in a if (x ** 3) % 10 == 0])
c = []
for i in range(len(a) - 2):
    if abs((m - (a[i] + a[i+1] + a[i+2])) ** 2) % 2 == 0 and abs((m - (a[i] + a[i+1] + a[i+2])) ** 2) % 10 == 0:
        c.append(min(a[i], a[i+1], a[i+2]))
print(len(c), min(c))