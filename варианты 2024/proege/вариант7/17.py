b = []
a = [int(x) for x in open('17.txt')]
m121 = max([x for x in a if str(x)[-3:] == '121'])
for i in range(len(a) - 2):
    z = a[i:i+3]
    s = [x for x in z if 1000 <= abs(x) <= 9999 and abs(x) % 2 == 0]
    if len(s) <= 1 and sum(z) <= m121:
        b.append(sum(z))
print(len(b), max(b))