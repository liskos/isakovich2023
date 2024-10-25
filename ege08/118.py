import itertools

k = set()

for i in itertools.permutations('123431'):
    ss = ''.join(i)
    if '11' not in ss and '33' not in ss:
        k.add(ss)



print(len(k))
