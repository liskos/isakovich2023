a = open('24data/24-296.txt').read()

m = 320
for left in range(len(a)):
    for right in range(left + m, len(a)):
        t = a[left:right]
        if t.count('CD') == 160:
            m = max(len(t), m)
        elif t.count('CD') > 160:
            break
print(m)
