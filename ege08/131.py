import itertools

k=set()

for s in itertools.permutations('2Р12Л', r=5):
    ss = ''.join(s)
    ss = ss.replace('2', '1')
    if '11' not in ss:
        k.add(s)
print(len(k))
