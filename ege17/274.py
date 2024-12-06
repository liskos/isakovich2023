

a = [int(x) for x in open('17data/17-274.txt')]
ma = max([x for x in a])

c = []
for i in range(len(a) - 1):
    if abs(a[i]) + abs(a[i+1]) > 17043 and (abs(a[i]) + abs(a[i+1])) % 3 == 0:
        c.append(a[i] + a[i+1])
print(len(c), min(c))