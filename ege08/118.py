import itertools

k = 0

for i in itertools.permutations('123431'):
    ss = ''.join(i)
    if '11' not in ss and '33' not in ss:
        k+=1



print(k)
