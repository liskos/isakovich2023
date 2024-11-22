
a = [int(x) for x in open('17data/17-10.txt')]
c = []
for i in range(len(a) - 2):
    if (a[i] == 90) or (a[i+1] == 90) or (a[i+2] == 90):
        c.append(max(a[i], a[i+1], a[i+2]))
print(len(c), sum(c))