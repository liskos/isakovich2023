

a = [int(x) for x in open('17data/17-276.txt')]


c = []
for i in range(len(a) - 2):
    t = sorted(a[i:i+3])
    if t[1] * t[1] == t[0] * t[2] and t[1] / t[0] > 1:
        c.append((t[1] / t[0]) ** 2)
print(len(c), max(c))