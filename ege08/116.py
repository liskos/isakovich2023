import itertools

k = 0

for i in itertools.permutations('123451'):
    ss = ''.join(i)
    if '11' not in ss:
        k+=1



print(k)