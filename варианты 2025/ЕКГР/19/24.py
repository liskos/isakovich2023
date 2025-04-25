a = open('24_21717.txt').read()
l = len(a)
t = [x for x in range(len(a)) if a[x:x+3] == 'RSQ']
k = 130
try:
    for i in range(len(t)):
        i2 = t[i+k-1] + 3
        while a[i2] == 'Q':
            i2 += 1
        if i2 > t[i+k]+1:
            continue
        l = min(l, i2 - i + 1)
except:
    pass
print(l)