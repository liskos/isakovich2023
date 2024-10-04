import itertools


k = 0
for s in itertools.permutations('НОДА'):
    ss = ''.join(s)
    if (('ОА' not in ss) and
            ('АО' not in ss) and ('НД' not in ss) and ('ДН' not in ss)):
        k += 1
        print(ss)
print(k)



