import itertools

k = 0

for i in itertools.permutations('ЧИУАУА'):
    ss = ''.join(i)
    k+=1



print(k)
#180