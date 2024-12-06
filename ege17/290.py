def f(d):
    n = []
    while d > 0:
        n.append(d % 5)
        d = d // 5
    return n[0] == 1

def sh(h):
    n = []
    while h > 0:
        n.append(h % 6)
        h = h // 6
    return len(n) == 4

a = [int(x) for x in open('17data/17-288.txt')]


c = []
for i in range(len(a) - 2):
    if (f(a[i]) or f(a[i+1]) or f(a[i+2])) and sh(a[i]) and sh(a[i+1]) and sh(a[i+2]):
        c.append(max(a[i], a[i+1], a[i+2]) - min(a[i], a[i+1], a[i+2]))
print(len(c), max(c))