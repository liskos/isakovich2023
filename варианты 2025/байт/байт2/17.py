a = [int(x) for x in open('17.txt')]

ma = max([x for x in a if abs(x) % 100 == 25 and len(str(abs(x))) == 5]) ** 2
c = []
for i in range(len(a) - 2):
    t = a[i:i+3]
    b = [x for x in t if abs(x) % 100 == 25 and len(str(abs(x))) == 5]
    if len(b) > 0 and a[i] ** 2 + a[i+1] ** 2 + a[i+2] ** 2 <= ma:
        c.append(a[i] ** 2 + a[i+1] ** 2 + a[i+2] ** 2)
print(len(c), min(c))