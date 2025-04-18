a = open('24data/24-309.txt').read()
m = 80 * 4

for left in range(len(a)):
    for right in range(left + m, len(a)):
        t = a[left:right]
        c = t.count('FSRQ')
        if c == 80:
            m = max(len(t), m)
        elif c > 80:
            break
print(m)