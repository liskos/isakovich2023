a = open('24.txt').read()

for x in 'GHIJKLMNOPQRSTUVWXYZ':
    a = a.replace(x, 'Z')
m = 30
for left in range(len(a)):
    for right in range(left + m, len(a)):
        t = a[left:right+1]
        if t.count('B') > 10 or a[left] == '0' or 'Z' in t:
            break
        elif t.count('B') == 10:
            if right-left+1 > m:
                m = right-left+1
                print(m, t)

print(m)
