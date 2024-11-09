import itertools

k=set()
for i in itertools.permutations('1ДЕК1Л1Н'):
    ss = ''.join(i)
    if '11' not in ss:
        print(ss)
        k.add(ss)
print(len(k))