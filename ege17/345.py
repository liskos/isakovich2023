
a = [int(x) for x in open('17data/17-345.txt')]
m = min([x for x in a if x % 100 == 52])
s = max([x for x in a if x % 100 == 52])
c = []
for i in range(len(a) - 1):
    if a[i] < (s - m) and not(a[i+1] < (s - m)):
        c.append(a[i] + a[i+1])
print(len(c), max(c))