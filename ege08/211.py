import itertools

k=set()
for i in itertools.permutations('1И01О0'):
    ss = ''.join(i)
    if '11' not in ss and '00' not in ss:
        k.add(ss)
print(len(k))