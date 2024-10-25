import itertools

k = 0

for i in itertools.permutations('ТАРТАР'):
    ss = ''.join(i)
    k+=1



print(k)
#360
