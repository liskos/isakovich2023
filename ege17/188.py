

a = [int(x) for x in open('17data/17-7.txt')]
c = []
for i in range(len(a) - 2):
    t = [x for x in a[i:i+3] if hex(x)[-1] == '0']
    if len(t) >= 2:
        c.append(max(a[i:i+3]))
print(len(c), sum(c))