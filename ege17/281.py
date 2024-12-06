

a = [int(x) for x in open('17data/17-281.txt')]


c = []
for i in range(len(a) - 5):
    t = a[i:i+6]
    k1 = t[1] - t[0]
    k2 = t[2] - t[1]
    k3 = t[4] / t[3]
    k4 = t[5] / t[4]
    k5 = t[5] - t[4]
    k6 = t[4] - t[3]
    k7 = t[1] / t[0]
    k8 = t[2] / t[1]
    if (k1 == k2 == k3 == k4 and k1 > 0  and k3 > 1) or (k5 == k6 == k7 == k8 and k5 > 0 and k7 > 1):
        c.append(sum(t))
print(len(c), max(c))