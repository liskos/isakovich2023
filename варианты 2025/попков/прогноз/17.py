a = [int(x) for x in open('17.txt')]

m = min([x for x in a if len(str(abs(x))) == 4 and abs(x) % 17 == 0]) ** 2

c=[]
for i in range(len(a) - 2):
    t = a[i:i+3]
    b = [x for x in t if len(str(abs(x))) == 4 and abs(x) % 100 == 27]
    if len(b) >= 1 and a[i] ** 2 + a[i+1] ** 2 + a[i+2] ** 2 <= m:
        c.append(abs(a[i]) + abs(a[i+1]) + abs(a[i+2]))

print(len(c), min(c))


