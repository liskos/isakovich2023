
def se(s):
    a = ''
    while s > 0:
        a += str(s % 7)
        s //= 7
    return a == a[::-1]
def sr(s):
    a = ''
    while s > 0:
        a += str(s % 7)
        s //= 7
    return a[::-1]


a = [int(x) for x in open('17data/17-10.txt')]
c = []
for i in range(len(a) - 1):
    if se(a[i] + a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), sr(max(c)))