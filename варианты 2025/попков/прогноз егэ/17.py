a = [int(x) for x in open('17.txt')]

mi = min([x for x in a if x > 0 and abs(x) % 10 == 8])
ma = max([x for x in a if abs(x) % 25 == 0])
h = []
for i in range(len(a) - 2):
    t = a[i:i+2]
    b = [x for x in t if len(str(abs(x))) == 4]
    c = [x for x in t if abs(x) % mi == 0]
    if len(b) == 2 and len(c) > 0 and a[i] + a[i+1] + a[i+2] >= ma:
        h.append(a[i] + a[i+1] + a[i+2])
print(len(h), max(h))

