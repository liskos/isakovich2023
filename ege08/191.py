import itertools

a = set()
for s, i in enumerate(itertools.product('САЛЬСА', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('А') <= 1:
        a.add(ss)

print(len(a))
