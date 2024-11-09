import itertools

k=set()
for i in itertools.permutations('МИМИКРИЯ'):
    ss = ''.join(i)
    k.add(ss)
print(len(k))