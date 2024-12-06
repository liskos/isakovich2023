

a = [int(x) for x in open('17data/17-271.txt')]
ma = sum([x for x in a]) // len([x for x in a])

c = []
for i in range(len(a) - 1):
    if (a[i] % 10) + (a[i+1] % 10) == 7 and a[i] < ma and a[i+1] < ma:
        c.append(a[i] + a[i+1])
print(len(c), max(c))