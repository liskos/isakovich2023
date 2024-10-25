import itertools

k = 0

for s, i in enumerate(itertools.product('В1НТ1ЛЬ', repeat=7), 1):
    ss = ''.join(i)
    if '1Ь1' not in ss and ss[-1] != 'Ь' and ss.count('В') == 1 and ss.count('Н') == 1 and ss.count('Т') == 1 and ss.count('Л') == 1 and ss.count('Ь') == 1:
        k += 1

print(k)
