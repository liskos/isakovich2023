import itertools

b = set()
for s, i in enumerate(itertools.permutations('КОМПЬЮТЕР', r=9), 1):
    ss = ''.join(i)
    if ss[-2] == 'Е' and ss[:4] == sorted(ss[:4]):
        b.add(ss)
print(len(b))
