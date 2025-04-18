a = open('24data/24-263.txt').read()

t = ''
m = 10**10
t_best = ""
for i in a:
    t += i
    while t[1:].count('FAT') + t[1:].count('BAD') >= 3:
        t = t[1:]
    if t.count('FAT') + t.count('BAD') == 3:
        if len(t) < m:
            m = len(t)
            t_best = t
print(m, t_best)