
a = [int(x) for x in open('17data/17-7.txt')]
c = []
for i in range(len(a)):
    if sum(int(x) for x in str(a[i])) % 3 == 0:
        c.append(a[i])
print(len(c), max(c))