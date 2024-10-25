import itertools

k=set()

for s in itertools.permutations('К1Б1Л1', r=6):
    ss = ''.join(s)
    if '11' not in ss:
        k.add(ss)
print(len(k))
