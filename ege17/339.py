
a = [int(x) for x in open('17data/17-339.txt')]
sr = min([x for x in a if x > 0 and x % 19 == 0])
c = []
for i in range(len(a) - 1):
    if a[i] + a[i+1] < sr:
        c.append(a[i] + a[i+1])
print(len(c), max(c))