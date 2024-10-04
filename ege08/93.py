import itertools


k = 0
for s, i in enumerate(itertools.product('ПАЙЩИК', repeat=6), 1):
    ss = ''.join(i)
    if (ss.count('П') == 1 and
            ss.count('А') == 1 and
            ss.count('Й') == 1 and
            ss.count('Щ') == 1 and
            ss.count('И') == 1 and
            ss.count('К') == 1 and
            'Й' not in ss[0] and
            'ИА' not in ss):
        k += 1
        print(s, ss)
print(k)



