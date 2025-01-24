import itertools
c = set()

for i in itertools.permutations('ПАРИЖАНКА'):
    ss = ''.join(i)
    if ss.count('АА') == 1:
        c.add(ss)
print(len(c))