import itertools


k = 0
for s, i in enumerate(itertools.product('НИГРОЛ', repeat=6), 1):
    ss = ''.join(i)
    if (ss.count('Н') == 1 and
            ss.count('И') == 1 and
            ss.count('Г') == 1 and
            ss.count('Р') == 1 and
            ss.count('О') == 1 and
            ss.count('Л') == 1 and
            'О' not in ss[0] and
            'ОИГ' not in ss):
        k += 1
        print(s, ss)
print(k)



