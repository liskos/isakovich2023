import itertools


k = 0
for s, i in enumerate(itertools.product('КАБИНЕТ', repeat=7), 1):
    ss = ''.join(i)
    if (ss.count('К') == 1 and
            ss.count('А') == 1 and
            ss.count('Б') == 1 and
            ss.count('И') == 1 and
            ss.count('Н') == 1 and
            ss.count('Е') == 1 and
            ss.count('Т') == 1 and
            'Б' not in ss[0] and
            'ЕА' not in ss):
        k += 1
        print(s, ss)
print(k)



