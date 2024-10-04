import itertools


k = 0
for s, i in enumerate(itertools.product('КОМБАЙН', repeat=7), 1):
    ss = ''.join(i)
    if (ss.count('К') == 1 and
            ss.count('О') == 1 and
            ss.count('М') == 1 and
            ss.count('Б') == 1 and
            ss.count('А') == 1 and
            ss.count('Й') == 1 and
            ss.count('Н') == 1 and
            'Й' not in ss[0] and
            'АЙ' not in ss):
        k += 1
        print(s, ss)
print(k)



