a = [int(x) for x in open('17.txt')]
m = min(a)
c = []
for i in range(len(a) - 2):
    t = a[i:i+3]
    if (len([x for x in t if x > 0]) < len([x for x in t if x < 0])) and str(sum(t))[-1]== str(m)[-1]:
        c.append(abs(sum(t)))
print(len(c), max(c))