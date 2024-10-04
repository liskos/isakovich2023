import itertools


k = 0
for s, i in enumerate(itertools.product('НИЧЬЯ', repeat=5), 1):
    ss = ''.join(i)
    if (ss.count('Н') == 1 and
            ss.count('И') == 1 and
            ss.count('Ч') == 1 and
            ss.count('Ь') == 1 and
            ss.count('Я') == 1 and
            'Ь' not in ss[0] and
            'ЬИЯ' not in ss):
        k += 1
        print(s, ss)
print(k)



