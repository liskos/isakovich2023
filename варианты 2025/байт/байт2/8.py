import itertools


for i, s in enumerate(itertools.product('РПОГА', repeat=5), 1):
    ss = ''.join(s)
    if ss not in 'ОА' and ss.count('Г') == 2 and 'ГГ' not in ss and ss[0] != 'Р':
        print(i, ss)
        break