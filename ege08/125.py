import itertools

k = 0

for i in itertools.permutations('ТРАТАТА'):
    ss = ''.join(i)
    k+=1



print(k)
#840