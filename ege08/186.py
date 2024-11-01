import itertools

a = set()
for s, i in enumerate(itertools.product('БАЛОН', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('А') <= 1 and ss.count('О') <= 1:
        a.add(ss)

print(len(a))
