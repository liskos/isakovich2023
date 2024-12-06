
a = [int(x) for x in open('17data/17-1.txt')]
sr = min([x for x in a if x > 0 and x % 15 == 0])
c = []
for i in range(len(a) - 1):
    if a[i] % 2 > 0 and a[i+1] % 2 > 0 and ((a[i] + a[i+1]) // 2) >= sr:
        c.append((a[i] + a[i+1]) // 2)
print(len(c), min(c))