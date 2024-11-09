import itertools

k=set()
for i in itertools.permutations('КЛ1БХ1УС'):
    ss = ''.join(i)
    if '11' not in ss:
        k.add(ss)
print(len(k))