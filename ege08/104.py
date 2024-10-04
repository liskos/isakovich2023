import itertools


k = 0
for s, i in enumerate(itertools.product('НАДПИСЬ', repeat=7), 1):
    ss = ''.join(i)
    if (ss.count('Н') == 1 and
            ss.count('А') == 1 and
            ss.count('Д') == 1 and
            ss.count('П') == 1 and
            ss.count('И') == 1 and
            ss.count('С') == 1 and
            ss.count('Ь') == 1 and
            'Ь' not in ss[0] and
            'ЬИА' not in ss):
        k += 1
        print(s, ss)
print(k)



