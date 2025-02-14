a = [int(x) for x in open('17.txt')]

c = sum([x for x in a if abs(x) > 999])

d = []
for i in range(len(a)-2):
    if (a[i] > 99 or a[i+1] > 99 or a[i+2] >99) and a[i] * a[i+1] * a[i+2] > c:
        d.append(a[i] * a[i+1] * a[i+2])
print()