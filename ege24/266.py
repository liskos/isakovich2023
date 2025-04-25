a = open('24data/24-263.txt').read()


m = 120
for left in range(len(a)):
    for right in range(left+m, len(a)):
        t = a[left:right]
        if t.count('Z') >= 120:
            m = min(len(t), m)
            break
print(m)