import itertools

k = set()

for i in itertools.permutations('ТАРТАР'):
    ss = ''.join(i)
    k.add(ss)



print(len(k))
#360
