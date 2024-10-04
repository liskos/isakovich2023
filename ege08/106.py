import itertools


k = 0
for s, i in enumerate(itertools.product('НОДА', repeat=4), 1):
    ss = ''.join(i)
    if (ss.count('Н') == 1 and
            ss.count('О') == 1 and
            ss.count('Д') == 1 and
            ss.count('А') == 1 and
            'ОО' not in ss and
            'АА' not in ss or 'НН' not in ss and 'ДД' not in ss):
        k += 1
        print(s, ss)
print(k)



