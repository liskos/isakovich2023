
a = [int(x) for x in open('17data/17-336.txt')]
sr = min([x for x in a if x % 8 == 0 and x != 8])
c = []
for i in range(len(a) - 1):
    if a[i] % sr == 0 and a[i] % sr == 0:
        c.append(a[i] + a[i+1])
print(len(c), min(c))