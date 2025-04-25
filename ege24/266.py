a = open('24data/24-263.txt').read()

l = len(a)
t = [x for x in range(len(a)) if a[x] == 'Z']
print(t)
k = 120
try:
    for i in range(len(t) - (k-1)):
        l = min(t[i + k - 1] - t[i] + 1, l)
except:
    pass
print(l)