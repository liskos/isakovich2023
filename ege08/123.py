import itertools

k = set()

for i in itertools.permutations('АССАСИН'):
    ss = ''.join(i)
    k.add(ss)



print(len(k))
#1008
