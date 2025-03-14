a = [int(x) for x in open('17.txt')]

sr = sum([x for x in a]) / len(a)

c = []
for i in range(len(a) - 2):
    if (a[i] ** 2 + a[i+1] ** 2 + a[i+2] ** 2) % 19 == 0:
        c.append(a[i] * a[i+1] * a[i+2])
