

a = [int(x) for x in open('17data/17-7.txt')]
c = []
for i in range(len(a)):
    if hex(a[i])[-1] == '9' and hex(a[i])[-2] != 'A':
        c.append(a[i])
print(len(c), max(c))