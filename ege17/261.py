a = [int(x) for x in open('17data/17-257.txt')]
mm = max([x for x in a if x % 2 > 0])
c = []
for i in range(len(a) - 1):
    if 2 * (a[i] + a[i + 1]) > mm:
        c.append(a[i] + a[i + 1])
print(len(c), min(c))
