a = [int(x) for x in open('17.txt')]


ma = max([x for x in a if len(str(abs(x))) == 4])

c = []
for i in range(len(a) - 1):
    t = a[i:i+2]
    b = [x for x in t if x <= ma]
    if len(b) == 1 and abs(a[i] ** 2 + a[i+1] ** 2) % 100 == 12:
        c.append(a[i] ** 2 + a[i+1] ** 2)

print(len(c), min(c))