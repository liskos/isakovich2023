import itertools


k = 0
for s, i in enumerate(itertools.product('КОМЕТА', repeat=6), 1):
    ss = ''.join(i)
    if (ss.count('К') == 1 and
            ss.count('О') == 1 and
            ss.count('М') == 1 and
            ss.count('Е') == 1 and
            ss.count('Т') == 1 and
            ss.count('А') == 1 and
            'ОО' not in ss and
            'ЕЕ' not in ss and 'АА' not in ss or 'КК' not in ss and 'ММ' not in ss and 'ТТ' not in ss):
        k += 1
        print(s, ss)
print(k)



