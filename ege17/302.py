

a = [int(x) for x in open('17data/17-302.txt')]
mi = min([x for x in a if x % 21 == 0])
c = []
for i in range(len(a) - 1):
    if (abs((a[i] + a[i+1] // 2) - mi) ** 2) % 10 == 0:
        c.append(a[i] * a[i+1])
print(len(c), min(c))