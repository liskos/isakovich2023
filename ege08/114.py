import itertools

k = set()

for i in itertools.permutations('1213'):
    ss = ''.join(i)
    if '11' not in ss:
        k.add(ss)



print(len(k))
