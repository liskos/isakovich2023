

a = [int(x) for x in open('17data/17-1.txt')]
sr = sum(a) / len(a)
c = []
for i in range(len(a) - 2):
    t = [x for x in a[i:i+3] if x < sr]
    t2 = [x for x in a[i:i+3] if abs(x) % 10 == 4]
    if len(t) >= 1 and len(t2) >= 2:
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))