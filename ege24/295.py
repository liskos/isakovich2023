a = open('24data/24-295.txt').read()

m = 320
for left in range(len(a)):
    for right in range(left + m, len(a)):
        t = a[left:right+1]
        if t.count('DE') <= 240:
            m = max(right-left+1, m)
        elif t.count('DE') > 240:
            break
print(m)
