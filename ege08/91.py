import itertools


k = 0
for s, i in enumerate(itertools.product('КАЛИЙ', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('К') == 1 and ss.count('А') == 1 and ss.count('Л') == 1 and ss.count('И') == 1 and ss.count('И') == 1 and 'Й' not in ss[0] and 'ИА' not in ss:
        k += 1
        print(s, ss)
print(k)



