a = open('24.txt').read()
m = 320
d = []
for left in range(len(a)):
    for right in range(left + m, len(a)):
        t = a[left:right]
        c = t.count('RSQ')
        if c == 130 and t[-1] != 'Q':
            m = max(len(t), m)
            d.append(m)
        elif c > 130:
            break
print(min(d), m)