import itertools
a=set()
for i in itertools.permutations('СПОРТЛОТО'):
    if i[0] == 'О' == i[-1]:
        a.add(i)
print(len(a))