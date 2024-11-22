
def se(s):
    a = []
    while s > 0:
        a.append(str(s % 7))
        s //= 7
    return int(''.join(a))


a = [int(x) for x in open('17data/17-10.txt')]
c = []
for i in range(len(a) - 1):
    if se(a[i]) + se(a[i+1]):
        c.append(se(a[i]) + se(a[i+1]))
print(len(c), max(c))