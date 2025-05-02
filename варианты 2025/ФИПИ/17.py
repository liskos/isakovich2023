a = [int(x) for x in open('17.txt')]
m = min([x for x in a if len(str(abs(x))) == 3 and abs(x) % 100 == 15]) ** 2

c = []
for i in range(len(a) - 2):
    if ((a[i] < 0 and a[i+1] < 0 and a[i+2] < 0) or (a[i] > 0 and a[i+1] > 0 and a[i+2] > 0)) and max(a[i],a[i+1],a[i+2]) * min(a[i],a[i+1],a[i+2]) > m:
        c.append(max(a[i],a[i+1],a[i+2]) * min(a[i],a[i+1],a[i+2]))
print(len(c), min(c))


