import itertools

a = set()
for s, i in enumerate(itertools.product('МЕЧТА', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('А') >= 3:
        a.add(ss)

print(len(a))