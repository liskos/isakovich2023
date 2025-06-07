a = [int(x) for x in open('17.txt')]


ma = min([x for x in a if abs(x) % 10 == abs(x) % 100 // 10 and len(str(abs(x))) == 5])
h = []
for i in range(len(a) - 2):
    t = a[i:i+3]
    b = [x for x in t if len(str(abs(x))) == 4]
    if len(b) <= 2 and a[i] + a[i+1] + a[i+2] >= ma:
        h.append(a[i]+a[i+1]+a[i+2])
print(len(h), max(h))

