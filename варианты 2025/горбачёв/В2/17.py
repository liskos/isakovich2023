a = [int(x) for x in open('17.txt')]

ot = [x for x in a if x < 0 and x % 5 == 0]
c= []
for i in range(len(a) - 2):
    t = [x for x in a[i:i+3] if len(str(abs(x))) == 4]
    if len(t) >= 2 and a[i] + a[i+1] + a[i+2] >= len(ot):
        c.append(a[i]+a[i+1]+a[i+2])

print(len(c), min(c))