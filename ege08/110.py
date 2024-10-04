import itertools


k = 0
for s, i in enumerate(itertools.product('РУЛЬКА', repeat=6), 1):
    ss = ''.join(i)
    if (ss.count('Р') == 1 and
            ss.count('У') == 1 and
            ss.count('Л') == 1 and
            ss.count('Ь') == 1 and
            ss.count('К') == 1 and
            ss.count('А') == 1 and
            'Ь' not in ss[0] and
            'УЬ' not in ss and 'АЬ' not in ss):
        k += 1
        print(s, ss)
print(k)



