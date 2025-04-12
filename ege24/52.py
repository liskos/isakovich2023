s = open('24data/k8-0.txt').read()

t = ''
tbest = ''
m = 0
for i in s:
    if not t:
        t = i
    elif t[-1] == i:
        t += i
    else:
        t = i
    if len(t) > len(tbest):
        tbest = t
        m = len(t)
print(tbest, m)