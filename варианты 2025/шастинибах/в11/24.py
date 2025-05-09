a = open('24.txt').read()

m = 30
for left in range(len(a)):
    for right in range(left + m, len(a)):
        t = a[left:right+1]
        if t.count('B') == 10:
            m = max(right-left+1, m)
        elif t.count('B') > 10:
            break
print(m)
