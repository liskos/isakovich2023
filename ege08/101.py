import itertools


k = 0
for s, i in enumerate(itertools.product('ШАНЕЛЬ', repeat=6), 1):
    ss = ''.join(i)
    if (ss.count('Ш') == 1 and
            ss.count('А') == 1 and
            ss.count('Н') == 1 and
            ss.count('Е') == 1 and
            ss.count('Л') == 1 and
            ss.count('Ь') == 1 and
            'Ь' not in ss[0] and
            'ЕАЬ' not in ss):
        k += 1
        print(s, ss)
print(k)



