def f(a):
    s1 = sum([int(x) for x in str(a) if x in '02468'])
    s2 = sum([int(x) for x in str(a) if x in '13579'])
    return s1 > s2

a = [int(x) for x in open('17data/17-304.txt')]

m = min([x for x in a if x % 2 == 0])
c = []
for i in range(len(a) - 1):
    if f(a[i]) and f(a[i+1]) and (a[i] + a[i+1]) % m == 0:
        c.append(a[i] + a[i+1])
print(len(c), max(c))