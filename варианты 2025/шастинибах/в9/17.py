a = [int(x) for x in open('17.txt')]

c = sum([x for x in a if len(str(abs(x))) == 4])

d = []
for i in range(len(a)-2):
    t = a[i:i+3]
    b = [x for x in t if len(str(abs(x))) == 3]
    if len(b) == 2 and a[i] * a[i+1] * a[i+2] > c:
        d.append(a[i] * a[i+1] * a[i+2])
print(len(d), abs(min(d)))