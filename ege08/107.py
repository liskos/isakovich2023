import itertools


k = 0
for s, i in enumerate(itertools.product('КЛОУН', repeat=5), 1):
    ss = ''.join(i)
    if (ss.count('К') == 1 and
            ss.count('Л') == 1 and
            ss.count('О') == 1 and
            ss.count('У') == 1 and
            ss.count('Н') == 1 and
            'ОО' not in ss and
            'УУ' not in ss or 'КК' not in ss and 'ЛЛ' not in ss and 'НН' not in ss):
        k += 1
        print(s, ss)
print(k)



