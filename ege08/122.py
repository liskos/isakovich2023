import itertools

k = set()

for i in itertools.permutations('МОЛОКО'):
    ss = ''.join(i)
    k.add(ss)



print(len(k))
#240
