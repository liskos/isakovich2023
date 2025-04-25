a = open('24data/24-263.txt').read()


m = 100
for left in range(len(a)):
    for right in range(left+m, len(a)):
        t = a[left:right]
        if t.count('Y') <= 150:
            m = max(len(t), m)
        elif t.count('Y') > 150:
            break
print(m)