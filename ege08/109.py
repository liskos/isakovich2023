import itertools


k = 0
for s, i in enumerate(itertools.product('АБРИКОС', repeat=7), 1):
    ss = ''.join(i)
    if (ss.count('А') == 1 and
            ss.count('Б') == 1 and
            ss.count('Р') == 1 and
            ss.count('И') == 1 and
            ss.count('К') == 1 and
            ss.count('О') == 1 and
            ss.count('С') == 1 and
            'АА' not in ss and
            'ИИ' not in ss and 'ОО' not in ss or 'ББ' not in ss and 'РР' not in ss and 'КК' not in ss and 'СС' not in ss):
        k += 1
        print(s, ss)
print(k)



