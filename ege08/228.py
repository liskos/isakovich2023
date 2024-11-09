import itertools

k=set()
for i in itertools.permutations('МАРИНА'):
    ss = ''.join(i)
    if ss[0] not in 'АИ':
        print(ss)
        k.add(ss)
print(len(k))