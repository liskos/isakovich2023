import itertools


k = 0
for s, i in enumerate(itertools.product('КУПЧИХА', repeat=7), 1):
    ss = ''.join(i)
    if (ss.count('К') == 1 and
            ss.count('У') == 1 and
            ss.count('П') == 1 and
            ss.count('Ч') == 1 and
            ss.count('И') == 1 and
            ss.count('Х') == 1 and
            ss.count('А') == 1 and
            'Ч' not in ss[0] and
            'ИАУ' not in ss):
        k += 1
        print(s, ss)
print(k)



