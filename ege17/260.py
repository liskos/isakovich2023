a = [int(x) for x in open('17data/17-257.txt')]
mm = [x for x in a if x % 10 == 4]
c = []
for i in range(len(a) - 1):
    if a[i] + a[i + 1] < max(mm) + min(mm):
        c.append(a[i] + a[i + 1])
print(len(c), max(c))