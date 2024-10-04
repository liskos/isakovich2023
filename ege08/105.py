import itertools


k = 0
for s, i in enumerate(itertools.product('НОБЕЛИЙ', repeat=7), 1):
    ss = ''.join(i)
    if (ss.count('Н') == 1 and
            ss.count('О') == 1 and
            ss.count('Б') == 1 and
            ss.count('Е') == 1 and
            ss.count('Л') == 1 and
            ss.count('И') == 1 and
            ss.count('Й') == 1 and
            'Й' not in ss[0] and
            'ИЙО' not in ss):
        k += 1
        print(s, ss)
print(k)



