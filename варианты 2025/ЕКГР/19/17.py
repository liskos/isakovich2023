a = [int(x) for x in open('17.txt')]

m = min([x for x in a if len(str(abs(x))) == 4 and abs(x) % 10 == 6 and x > 0])
c = []
for i in range(len(a) - 2):
    t = a[i:i+3]
    b = [x for x in t if len(str(abs(x))) == 4 and abs(x) % 10 == 6]
    if len(b) == 1 and a[i] + a[i+1] + a[i+2] <= m:
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))