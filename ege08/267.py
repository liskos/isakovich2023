import itertools

b = []
for s, i in enumerate(itertools.permutations('СПОРТЛОТО'), 1):
    ss = ''.join(i)
    if ss[0] not in 'О' and ss[-1] not in 'О':
        b.append(ss)
        r = sorted(b)
print()
