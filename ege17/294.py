

a = [int(x) for x in open('17data/17-294.txt')]
sr = sum([x for x in a]) // len([x for x in a])

c = []
for i in range(len(a) - 1):
    if a[i] + a[i+1] > sr:
        c.append(a[i] + a[i+1])
print(len(c), max(c))