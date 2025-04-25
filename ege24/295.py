a = open('24data/24-296.txt').read()

m = 320
for left in range(len(a)):
    for right in range(left + m, len(a)):
        t = a[left:right]
        if t.count('DE') <= 240:
            m = max(len(t), m)
        elif t.count('DE') > 240:
            break
print(m)
