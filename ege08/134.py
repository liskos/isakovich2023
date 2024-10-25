import itertools

k=set()

for s in itertools.permutations('В2Р2Т1', r=6):
    ss = ''.join(s)
    ss = ss.replace('2', '1')
    if '11' not in ss:
        k.add(s)
print(len(k))
