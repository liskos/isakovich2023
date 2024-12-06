

a = [int(x) for x in open('17data/17-282.txt')]
ma = max([x for x in a if x % 41 == 0])

c = []
for i in range(len(a) - 1):
    if a[i] + a[i+1] < ma:
        c.append(a[i] + a[i+1])
print(len(c), max(c))