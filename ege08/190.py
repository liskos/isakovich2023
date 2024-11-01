import itertools

a = set()
for s, i in enumerate(itertools.product('КАЛЬКА', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('А') <= 1:
        a.add(ss)

print(len(a))
