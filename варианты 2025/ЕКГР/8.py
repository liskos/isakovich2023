import itertools


for i, s in enumerate(itertools.product('АВНРЬЯ', repeat=5), 1):
    ss = ''.join(s)
    if ss[0] != 'Я' and 'ЯЯ' not in ss and ss.count('Ь') <= 1:
        print(i, ss)
