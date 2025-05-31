a = [int(x) for x in open('17.txt')]


ma = max([x for x in a if abs(x) % 100 == 52 and len(str(abs(x))) == 4]) * 3
h = []
for i in range(len(a) - 2):
    t = a[i:i+3]
    b = [x for x in t if x > 0]
    if len(b) >= 2 and max(a[i], a[i+1], a[i+2]) ** 2 + min(a[i], a[i+1], a[i+2]) ** 2 > ma ** 2:
        h.append(abs(max(a[i], a[i+1], a[i+2]) ** 3 + min(a[i], a[i+1], a[i+2]) ** 3))
print(len(h), min(h))

