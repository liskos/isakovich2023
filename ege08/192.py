import itertools

a = set()
for s, i in enumerate(itertools.product('МАРИНА', repeat=8), 1):
    ss = ''.join(i)
    if 'Н' not in ss[:4] and ss[:4].count('М') == 1 and ss[:4].count('А') == 1 and ss[:4].count('Р') == 1 and ss[:4].count('И') == 1 and ss[4:].count('М') == 0 and ss[4:].count('Р') == 0 and ss in 'МАРИАННА':
        print(s, ss)



