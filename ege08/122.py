import itertools

k = 0

for i in itertools.permutations('МОЛОКО'):
    ss = ''.join(i)
    k+=1



print(k)
#240
