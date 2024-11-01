import itertools

a = set()
for s, i in enumerate(itertools.product('САКУРА', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('А') <= 1 and ss.count('У') <= 1:
        a.add(ss)

print(len(a))
