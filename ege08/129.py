import itertools

k=set()

for s in itertools.permutations('В1Р1Н', r=5):
    ss = ''.join(s)
    if '11' not in ss:
        k.add(ss)
print(len(k))
