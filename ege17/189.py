
def tr(s):
    a = []
    while s > 0:
        a.append(s % 3)
        s //= 3
    return a


a = [int(x) for x in open('17data/17-7.txt')]
c = []
for i in range(len(a) - 2):
    if tr(a[i])[0] == 2 or tr(a[i+1])[0] == 2 or tr(a[i+2])[0] == 2:
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))