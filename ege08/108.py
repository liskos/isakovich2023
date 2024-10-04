import itertools


k = 0
for s in itertools.permutations('000111'):
    ss = ''.join(s)
    if ('00' not in ss) and ('11' not in ss):
        k += 1
        print(ss)
print(k)



