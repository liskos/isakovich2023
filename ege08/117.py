import itertools

k = set()

for i in itertools.permutations('124131'):
    ss = ''.join(i)
    if '11' not in ss:
        k.add(ss)



print(len(k))
