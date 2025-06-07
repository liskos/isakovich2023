a = open('24.txt').read()
m = 400 * 4

for left in range(len(a)):
    for right in range(left + m, len(a)):
        t = a[left:right]
        c = t.count('LND')
        if c <= 10000:
            m = max(len(t), m)
        elif c >= 10000:
            break
print(m)