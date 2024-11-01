import itertools


k = 0
for i in itertools.product('АВИКНСТ', repeat=4):
    ss = ''.join(i)
    if ss[0] not in 'АИ' and ss[-1] in 'АИ':
        k+=1
        if ss == 'НИКА':
            print(k, ss)
