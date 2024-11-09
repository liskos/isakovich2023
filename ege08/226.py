import itertools

k=set()
for i in itertools.permutations('КУСАТЬ', r=5):
    ss = ''.join(i)
    if ss[0] != 'Ь' and 'СУК' not in ss:
        print(ss)
        k.add(ss)
print(len(k))