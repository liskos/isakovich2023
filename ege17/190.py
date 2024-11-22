
def tr(s):
    a = []
    while s > 0:
        a.append(s % 8)
        s //= 8
    return a

a = [int(x) for x in open('17data/17-7.txt')]
c = []
for i in range(len(a)):
    if tr(a[i])[-1] == 7 and tr(a[i])[-1] != 27:
        c.append(a[i])
print(len(c), max(c))