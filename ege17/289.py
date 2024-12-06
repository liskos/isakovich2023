def f(d):
    n = []
    while d > 0:
        n.append(d % 7)
        d = d // 7
    return n[0] != 3

a = [int(x) for x in open('17data/17-288.txt')]


c = []
for i in range(len(a) - 3):
    if (abs(a[i]) % 10 == 3 or abs(a[i+1]) % 10 == 3 or abs(a[i+2]) % 10 == 3 or abs(a[i+3]) % 10 == 3) and f(a[i]) and f(a[i+1]) and f(a[i+2]) and f(a[i+3]):
        c.append(max(a[i], a[i+1], a[i+2], a[i+3]) - min(a[i], a[i+1], a[i+2], a[i+3]))
print(len(c), min(c))